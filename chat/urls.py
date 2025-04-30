from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path('chat/<str:room_name>/', views.room, name='room'),
    path("", views.landpage, name="landpage"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("login/", views.login, name="login"),
    path("profile/", views.profile, name="profile"),
    path("registration/", views.registration, name="registration"),
    path("guest/", views.guest, name="guest"),
    path("logout/", views.logout, name="logout"),
    path("cancel/", views.cancel, name="cancel"),
    path("error/<str:id>/", views.error, name="error"),
    path("data_visualization/", views.data_visualization, name="data_visualization"),
    path("history/", views.history, name="history"),
    path("upload/", views.upload, name="upload"),
    path("uploaded/<str:meetingID>/", views.uploaded, name="uploaded"),

]
