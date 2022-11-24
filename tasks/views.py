from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
#from forms import Registeruser

# Create your views here.
def helloworld(request):

    return render(request, 'singup.html', {
        'form': UserCreationForm,
    })


def singup(request):
    return HttpResponse("hola")
    