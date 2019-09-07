from django import forms

from tickets.models import Bug, Feature, Comment


class TicketForm(forms.Form):
    """Ticket creation form"""
    title = forms.CharField(label="Give your issue a title")
    description = forms.CharField(label="Description of the issue", widget=forms.Textarea)
    type = forms.ChoiceField(label="What type of ticket is this?",
                             choices=[('bug', 'Bug'),
                                      ('feature', 'Feature')],
                             widget=forms.RadioSelect)


class BugForm(forms.ModelForm):
    """Bug form"""
    title = forms.CharField(label="Give your issue a title")
    description = forms.CharField(label="Description of the issue", widget=forms.Textarea)
    status = forms.ChoiceField(label="What is the status of this bug?",
                               choices=Bug.STATUS_CHOICES,
                               widget=forms.Select)

    class Meta:
        model = Bug
        fields = ['title', 'description', 'status']


class FeatureForm(forms.ModelForm):
    """Feature form"""
    title = forms.CharField(label="Give your issue a title")
    description = forms.CharField(label="Description of the issue", widget=forms.Textarea)
    status = forms.ChoiceField(label="What is the status of this feature?",
                               choices=Feature.STATUS_CHOICES,
                               widget=forms.Select)

    class Meta:
        model = Feature
        fields = ['title', 'description', 'status']


class CommentForm(forms.Form):
    content = forms.CharField(label="Comment", widget=forms.Textarea)
