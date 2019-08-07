from django.shortcuts import render, redirect

from .forms import ToDoForm
from .models import ToDo

# Create your views here.
def index(request):
    mytodo = ToDo.objects.order_by('id')

    form = ToDoForm()

    context = { 'mytodo': mytodo, 'form': form}

    return render(request, 'index.html', context)

