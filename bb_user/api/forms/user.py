from django import forms
from django.contrib.auth import get_user_model
from django.http import JsonResponse


class CreateForm(forms.ModelForm):
    confirm_password = forms.CharField(required=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')

    def clean(self):
        cleaned_data = super(CreateForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
        return cleaned_data
