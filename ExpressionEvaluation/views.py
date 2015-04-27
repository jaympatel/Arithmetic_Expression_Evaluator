from django.shortcuts import render
from django.http import HttpResponse
from .forms import ExpressionForm
from django.http import HttpResponseRedirect
from .models import Expression
from Evaluator import Evaluator


# Create your views here.


def get_expression(request):
    if request.method == 'POST':
        form = ExpressionForm(request.POST)
        if form.is_valid():
            expression=form.cleaned_data['expression']
            print form.cleaned_data['expression']
            # e = Expression()
            # e.expression_string=form.cleaned_data['expression']
            # e.expression_result='patel'
            # e.save()
            e = Evaluator()
            result=e.evaluate_string(expression)
            print result
            return render(request,'result.html',{'result':result})
                
    else:
        form = ExpressionForm()
        return render(request, 'index.html', {'form': form})



'''
def index(request):
    return HttpResponse('Hello from Python!')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

'''