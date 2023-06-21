from django import forms


class WaitForm(forms.Form):
    seconds = forms.IntegerField(label="wait")
