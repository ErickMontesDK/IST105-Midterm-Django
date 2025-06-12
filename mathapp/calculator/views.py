from django.shortcuts import render
from .forms import CalculatorForm

def calculate_view(request):
    form = CalculatorForm(request.POST or None)
    error = result = extra_logic = None 

    if request.method == 'POST' and form.is_valid():
        a = form.cleaned_data['input1']
        b = form.cleaned_data['input2']
        operation = form.cleaned_data['operation']

        if operation == 'add':
            result = a + b
            operation = "Addition"
        elif operation == 'sub':
            result = a - b
            operation = "Substraction"
        elif operation == 'mul':
            result = a * b
            operation = "Multiplication"
        elif operation == 'div':
            operation = "Division"
            if b != 0:
                result = a / b
            else:
                error = "Division by zero is not allowed"
        else:
            error = "Invalid operation"

        if error is None:

            if result > 100:
                extra_logic = result * 2
            
            if result < 0:
                extra_logic = result + 50
                
        

        return render(request, 'result.html', {'input1':a,'input2':b, 'operation':operation,'result': result, "extra_logic":extra_logic, 'error': error, 'form': form})

    return render(request, 'math_form.html', {'form': form})
