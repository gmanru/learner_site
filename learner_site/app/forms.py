from django import forms


class ContactForm(forms.Form):
    email = forms.CharField(label='Введите ваш email', widget=forms.Textarea())
    message = forms.CharField(label='Ваше сообщение', widget=forms.Textarea())
