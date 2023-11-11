from django import forms


class TransactionForm(forms.Form):
    value = forms.DecimalField(max_digits=11, decimal_places=2)
    sender_profile_id = forms.IntegerField()
    reciever_profile_id = forms.IntegerField()
    