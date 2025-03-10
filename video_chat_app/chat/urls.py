from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path('chat/<str:room_name>/', views.room, name='room'),
    path("", views.login, name="login"),
    path("registration/", views.registration, name="registration"),
    path("password/", views.password, name="password"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
