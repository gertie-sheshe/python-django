from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'videorequest/index.html')

def requestform(request):
    return render(request, 'videorequest/requestform.html')
