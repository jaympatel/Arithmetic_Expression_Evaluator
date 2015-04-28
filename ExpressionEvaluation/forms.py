
from django import forms

class ExpressionForm(forms.Form):

    expression = forms.CharField(label='', max_length=1000)