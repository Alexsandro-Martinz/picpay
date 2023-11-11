from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models.profile import Profile

from django.shortcuts import get_object_or_404

from api.models.transactions import Transactions
from api.serializers import TransactionSerializer
from api.services.notification_services import NotificationService
from api.services.transactions_services import TransactionService


@api_view(['GET', 'POST'])
def transactions_list(request):
    """
    List all code transactios, or create a new trasaction.
    """
    if request.method == 'GET':
        transactions = Transactions.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
        
        # checar se os dados são validos
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # verificar se o sender e o receiver estão cadastrados
        try:
            sender_id = serializer.validated_data.get('sender_profile_id')
            sender_profile = Profile.objects.get(pk=sender_id)
        except Profile.DoesNotExist:
            return Response({f'error':'Sender com o id: {sender_id} não foi encontrado'})
        
        # verifica se o profile_type do profile sender é diferente do tipo MERCHANT
        if sender_profile.profile_type == Profile.ProfileType.MERCHANT:
            return Response("Usuários do tipo comerciante não podem fazer transferências",status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            receiver_id = serializer.validated_data.get('receiver_profile_id')
            receiver_profile = Profile.objects.get(pk=receiver_id)
        except Profile.DoesNotExist:
            return Response({f'error':'Receiver com o id: {receiver_id} não foi encontrado'})

        # verificar se o sender tem saldo suficiente pra fazer a trasação
        amount = serializer.validated_data.get('amount')
        if not TransactionService.is_balance_enough_for_transaction(
            sender_balance=sender_profile.balance,
            transaction_amount=amount):
            return Response({'detail':'Saldo insuficiente para a trasação'},status=status.HTTP_401_UNAUTHORIZED)
            
        # consultar um sistema externo se a transação está autorizada          
        if not TransactionService.authorize_trasaction(sender_profile, amount):
            raise Exception('Trasação não autorizada', status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            transaction = Transactions(
                amount = amount,
                sender_profile_id = sender_profile.id,
                receiver_profile_id = receiver_profile.id)
            
            sender_profile.balance = sender_profile.balance - amount
            receiver_profile.balance = receiver_profile.balance + amount
        except Exception as e:
            print(f"Erro ao criar transação {e}")
        else:
            transaction.save(force_insert=True)
            sender_profile.save()
            receiver_profile.save()
            
            data = TransactionSerializer(transaction).data
            NotificationService.send_notification(
                sender_profile,
                "Trasação realizada com sucesse, você acaba de fazer uma transferencia.")
            NotificationService.send_notification(
                receiver_profile,
                "Trasação realizada com sucesso, você acaba de receber uma transferencia")
            return Response(data)
          
    
@api_view(['GET','PUT', 'DELETE'])
def transactions_detail(request, pk):
    
    try:
        transaction = Transactions.objects.get(pk=pk)
    except Transactions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    