from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
import json

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
    else:
        form = UserCreationForm()
    return render(request, 'SignUp.html', {'form': form})
def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'ChatRoom.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })