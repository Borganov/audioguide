from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=50, required=True)
    name = forms.CharField(label='Name', max_length=50, required=True)
    email = forms.EmailField(label='Email', max_length=50, required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'cols':24}), required=True)