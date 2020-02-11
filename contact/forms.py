from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'contactForm_field'}))
    name = forms.CharField(label='Name', max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'contactForm_field'}))
    email = forms.EmailField(label='Email', max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'contactForm_field'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'cols':24,'class': 'contactForm_field'}), required=True)