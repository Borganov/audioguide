from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(label='Sujet', max_length=200, required=True)
    name = forms.CharField(label='Votre nom',max_length=200, required=True)
    email = forms.EmailField(label='Votre email',max_length=200, required=True)
    message = forms.CharField(label='Message',widget=forms.Textarea, required=True)