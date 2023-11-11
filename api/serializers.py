from api.models.profile import Profile
from api.models.transactions import Transactions

from rest_framework import serializers


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'email', 'balance', 'profile_type', 'document']


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transactions
        fields = ['id', 'amount', 'sender_profile_id', 'receiver_profile_id', 'timestamp']
    