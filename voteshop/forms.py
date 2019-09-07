from django import forms


class OrderForm(forms.Form):
    votecount = forms.IntegerField(min_value=1, max_value=100, required=True)
