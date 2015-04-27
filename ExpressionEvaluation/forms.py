__author__ = 'Jay'



from django import forms

class ExpressionForm(forms.Form):

    expression = forms.CharField(label='Enter Arithmetic Expression', max_length=1000)