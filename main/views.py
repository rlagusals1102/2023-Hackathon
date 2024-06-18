from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def sub1(request):
    return render(request, 'sub1.html')

def sub2(request):
    return render(request, 'sub2.html')

def sub3(request):
    return render(request, 'sub3.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)

            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def chat_room(request, room_name):
    return render(request, 'chat_room.html', {
        'room_name': room_name
    })
