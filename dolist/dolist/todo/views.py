from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .forms import ToDoForm
from .models import ToDo

# Create your views here.
def index(request):
    mytodo = ToDo.objects.order_by('id')
    form = ToDoForm()
    context = { 'mytodo': mytodo, 'form': form}

    return render(request, 'index.html', context)

@require_POST
def addNewToDo(request):
    form = ToDoForm(request.POST)

    if form.is_valid():
        my_new_todo = ToDo(todotext=request.POST['text'])
        my_new_todo.save()

        return redirect('index')

