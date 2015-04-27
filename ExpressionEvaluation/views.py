from django.shortcuts import render
from django.http import HttpResponse
from .forms import ExpressionForm
from django.http import HttpResponseRedirect
from .models import Expression
from Evaluator import Evaluator



def get_expression(request):
    if request.method == 'POST':
        form = ExpressionForm(request.POST)
        if form.is_valid():
            expression=form.cleaned_data['expression']
            print form.cleaned_data['expression']
            e2 = Expression()
            e2.expression_string=str(form.cleaned_data['expression'])
            
            e = Evaluator()
            result=e.evaluate_string(expression)
            e2.expression_result=result
            e2.save()
            print result
            return render(request,'result.html',{'result':result})
                
    else:
        form = ExpressionForm()
        return render(request, 'index.html', {'form': form})


def db(request):

    expressions = Expression.objects.all()

    return render(request, 'db.html', {'expresions': expressions})

