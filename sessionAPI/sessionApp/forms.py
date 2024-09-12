from django import forms

class SessionForm(forms.Form):
    name = forms.CharField()
    quantity = forms.IntegerField()
