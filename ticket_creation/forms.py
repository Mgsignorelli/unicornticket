from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    """Ticket creation form"""
    title = forms.CharField(label="Give your issue a title")
    description = forms.CharField(label="Description of the issue", widget=forms.Textarea)

    class Meta:
        model = Ticket
        fields = ['title', 'description']
