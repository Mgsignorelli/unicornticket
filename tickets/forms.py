from django import forms


class TicketForm(forms.Form):
    """Ticket creation form"""
    title = forms.CharField(label="Give your issue a title")
    description = forms.CharField(label="Description of the issue", widget=forms.Textarea)
    type = forms.ChoiceField(label="What type of ticket is this?", choices=[('bug', 'Bug')], widget=forms.RadioSelect)
