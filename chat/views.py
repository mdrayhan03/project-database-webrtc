from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from database import Database
import json
import matplotlib.pyplot as plt
import pandas as pd
import os
from django.conf import settings
from io import BytesIO
import base64

db = Database()

# Create your views here.
@csrf_exempt
def landpage(request) :
    if request.method == "POST" :
        meeting = request.POST.get("buzzID")
        response = db.find_existing_meeting(meeting)
        user = request.session.get("user")
        if response is not None :
            if user : 
                db.insert_new_history(response, user["_id"], 2)
            else :
                db.insert_new_history(response, "guest account", 2)
            return redirect("chat:room", room_name=meeting)
        else :
            return redirect("chat:error")
    return render(request, "chat/index.html")

@csrf_exempt
def dashboard(request):
    if request.method == "POST":
        if "createMeetingBtn" in request.POST:
            user = request.session.get("user")  # Check if user session exists
            if not user:
                return redirect("chat:login")

            time = request.POST.get("maxTime")
            member = request.POST.get("maxMembers")
            
            # Insert new meeting and history
            response = db.insert_new_meeting(user["_id"], time, member)
            db.insert_new_history(response, user["_id"], 1)
            
            return redirect("chat:room", room_name=response)
    if request.method == "POST":
        if "joinBuzzBtn" in request.POST:
            meeting = request.POST.get("buzzID")
            response = db.find_existing_meeting(meeting)
            if response is not None :
                user = request.session.get("user")
                db.insert_new_history(response, user["_id"], 1)
                return redirect("chat:room", room_name=meeting)
            else :
                return redirect("chat:error")
    
    return render(request, "chat/dashboard.html")

def room(request, room_name):
    return render(request, 'chat/meeting.html', {'room_name': room_name})

@csrf_exempt
def login(request) :
    if request.COOKIES.get("remember_me") == "true":
        return redirect("chat:dashboard")
    
    if request.method == "POST" : 
        email = request.POST.get("email")
        password = request.POST.get("password")
        remember = request.POST.get("rememberMe")
        loginresponse = db.find_login_user(email, password)
        request.session["user"] = loginresponse
        response = redirect("chat:dashboard")
        if remember == "on" :
            response.set_cookie("remember_me", "true", max_age=31536000, samesite='Lax', secure=False)
            response.set_cookie("user", json.dumps(loginresponse), max_age=31536000, samesite='Lax', secure=False)
        return response            
        
    return render(request, "chat/login.html")

@csrf_exempt
def profile(request) :
    data = request.session.get("user")
    if request.method == "POST" :
        name = request.POST.get("name")
        email = request.POST.get("email")
        data = db.update_user_info(request.session.get("user")["_id"], name, email)
        request.session["user"] = data
        response = render(request, "chat/profile.html", {"data" : data})
        if request.COOKIES.get("remember_me") == "true":
            response.set_cookie("user", json.dumps(data), max_age=31536000, samesite='Lax', secure=False)
        return response
    return render(request, "chat/profile.html", {"data" : data})

@csrf_exempt
def registration(request) :
    if request.method == "POST" :
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")

        if password == cpassword :
            db.insert_new_user(name, email, password)
            return redirect("chat:login")
    return render(request, "chat/signup.html")

@csrf_exempt
def guest(request) :
    return render(request, "chat/guest_join.html")

@csrf_exempt
def cancel(request) :
    if request.session.get("user") :
        return redirect("chat:dashboard")
    return redirect("chat:landpage")

@csrf_exempt
def logout(request) :
    response = redirect("chat:landpage")
    response.delete_cookie("remember_me")
    db.find_logout_user(request.session.get("user")["_id"])
    del request.session["user"]
    return response

def error(request) :
    return render(request, "chat/error.html")

@csrf_exempt
def data_visualization(request):
    # Path to the CSV file
    csv_path = os.path.join(settings.BASE_DIR, 'static', 'GGS_new.csv')
    
    # Read the CSV file using pandas
    df = pd.read_csv(csv_path)
    
    # Count male vs female occurrences in the "sex" column
    gender_counts = df["sex"].value_counts().rename({1: "Male", 2: "Female"})
    
    # Generate the bar plot
    plt.figure(figsize=(5, 4))
    plt.bar(gender_counts.index, gender_counts.values, color=["blue", "pink"])
    plt.xlabel("Gender")
    plt.ylabel("Number of Events")
    plt.title("Male vs Female Events")

    # Save plot to a BytesIO buffer to render as an image
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    buffer.close()

    # Pass the graph to the template
    return render(request, "chat/visualization.html", {"graph": image_base64})