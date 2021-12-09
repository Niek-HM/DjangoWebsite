from django import forms

class contactForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=24)
    last_name = forms.CharField(required=True, max_length=64)
    user_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)