from django import forms

class FormContato(forms.Form):
    nome = forms.CharField(label="Nome:")
    email = forms.EmailField(label="E-mail:")
    mensagem = forms.CharField(widget=forms.Textarea, max_length="250", label="Mensagem:")