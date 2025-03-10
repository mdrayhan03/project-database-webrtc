from django.shortcuts import render

# Create your views here.
def room(request, room_name):
    return render(request, 'chat/room.html', {'room_name': room_name})

def login(request) :
    return render(request, "chat/login.html")

def registration(request) :
    return render(request, "chat/registration.html")

def password(request) :
    return render(request, "chat/password.html")

def dashboard(request) :
    return render(request, "chat/dashboard.html")