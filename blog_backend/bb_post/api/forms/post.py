from django import forms


class CreateForm(forms.Form):

    subject = forms.CharField()
    content = forms.CharField()
