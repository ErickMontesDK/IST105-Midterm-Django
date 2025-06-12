from django import forms

class CalculatorForm(forms.Form):
    OPERATION_CHOICES = [
        ('add', 'Addition'),
        ('sub', 'Subtraction'),
        ('mul', 'Multiplication'),
        ('div', 'Division'),
    ]
    
    input1 = forms.FloatField(label='First Number')
    input2 = forms.FloatField(label='Second Number')
    operation = forms.ChoiceField(
        choices=OPERATION_CHOICES,
        label='Operation',
        widget=forms.Select()
    )