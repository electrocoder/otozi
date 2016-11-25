from django import forms

class QForm(forms.Form):
    q = forms.CharField(max_length=100)
