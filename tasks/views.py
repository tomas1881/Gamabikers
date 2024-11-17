from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from .models import Post
from .forms import VentaForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html',{
        'form': UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return  render(request, 'signup.html',{
                    'form': UserCreationForm,
                    "error": 'el usuario ya existe'
                 }) 
        return render(request, 'signup.html',{
            'form': UserCreationForm,
            "error": 'contraseña no coiciden'
        }) 
    

def tasks(request):
    return render(request, 'tasks.html')

def cerrar(request):  #cerrar la sesion(signoup-login)
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso')
            return redirect('home')  # Redirige a la página principal o dashboard
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'signin.html')

def venta_list(request):
    posts = Post.objects.all()
    return render(request, 'tasks.html', {'posts': posts})

def venta_create(request):
    try:
        vendedor= request.POST['Nombre_vendedor']
        marca= request.POST['marca']
        modelo= request.POST['año']
        descripcion= request.POST['descripcion']

        if vendedor=="" or marca=="":
            raise ValueError('los campos no uedesn estar vacios')
        
        post=Post(
            Nombre_vendedor=vendedor,
            marca=marca,
            año=modelo,
            descripcion=descripcion,
        )

        post.save()
        print(post)
        return HttpResponseRedirect(reverse("tasks"))
    except ValueError as err:
        return HttpResponseRedirect(reverse("tasks"))


def venta_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = VentaForm(request.POST, request.FILES, instance=post)  
        if form.is_valid():
            form.save()
            return redirect('venta_list')
    else:
        form = VentaForm(instance=post)
    return render(request, 'venta_form.html', {'form': form})

def venta_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('tasks') 
    return render(request, 'venta_confirm_delete.html', {'post': post})


