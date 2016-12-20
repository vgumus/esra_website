from django import forms


class NameForm(forms.Form):
    name = forms.CharField(label="Name", widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Name Here', 'class': 'form-control'}))


class EmailForm(forms.Form):
    e_mail = forms.EmailField(label="E-mail", widget=forms.EmailInput(
        attrs={'placeholder': 'email@example.com', 'class': 'form-control'}))


class MessageForm(forms.Form):
    message = forms.CharField(label="Message", widget=forms.Textarea(
        attrs={'placeholder': 'Please, message here', 'class': 'form-control'}))
