from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import TaskForm, Registeruser
from .models import task
from django.utils import timezone
from django.contrib.auth.decorators import login_required
#from forms import Registeruser

# Create your views here.


def home(request):

    return render(request, 'home.html', {
        'form': UserCreationForm,
    })


def singup(request):
    if request.method == 'GET':
        return render(request, 'singup.html', {
            'form': UserCreationForm,
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return redirect('task')
            except:
                return render(request, 'singup.html', {
                    'form': UserCreationForm,
                    'error': "El usuario ya existe"
                })

    return render(request, 'singup.html', {
        'form': UserCreationForm,
        'error': "las contraseñas no coinciden"
    })


@login_required
def tasks(request):
    tasks = task.objects.filter(user=request.user, datecompleted__isnull=True) 
    #tasks = task.objects.all() 

    return render(request, 'task.html', {
        'task': tasks
    })

@login_required
def tasks_completed(request):
    tasks = task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    #tasks = task.objects.all() 

    return render(request, 'task.html', {
        'task': tasks
    })



def singout(request):
    logout(request)
    return redirect('home')


def singin(request):
    if request.method == 'GET':
        return render(request, 'singin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'singin.html', {
                'form': AuthenticationForm,
                'error': "usuario o contraseña incorrecto"
            })
        else:
            login(request, user)
            return redirect('task')


def create_task(request):

    if request.method == 'GET':
        return render(request, 'create_task.html', {
        'form': TaskForm
        })
    else:
        form = TaskForm(request.POST)
        new_task = form.save(commit=False)
        new_task.user = request.user
        new_task.save()

        return render(request, 'create_task.html', {
        'form': TaskForm
        })
    

def task_detail(request, task_id):
    #tasks = get_object_or_404(task, pk = task_id)
    if request.method == 'GET':
        try:
            tasks = task.objects.get(pk = task_id, user = request.user)
        except:
            raise Http404("hola mundo cruel")
        form = TaskForm(instance=tasks)

        return render(request, 'task_detail.html', {
            'tasks': tasks,
            'form': form
        })
    else:
        try:
            tasks = get_object_or_404(task, pk = task_id, user = request.user)
            form = TaskForm(request.POST, instance=tasks)
            form.save()
            return redirect('task')
        except:
            return render(request, 'task_detail.html', {
            'tasks': tasks,
            'form': form,
            'error': "Error al actualizar"
        })

def complete_task(request, task_id):
    tasks = get_object_or_404(task, pk=task_id, user=request.user)
    if request.method == 'POST':
        tasks.datecompleted = timezone.now()
        tasks.save()
        return redirect('task')


def delete_task(request, task_id):
    tasks = get_object_or_404(task, pk=task_id, user=request.user)
    if request.method == 'POST':
        tasks.delete()
        return redirect('task')


