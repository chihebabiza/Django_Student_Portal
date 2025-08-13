from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if user.role == "student":
                return redirect("projects:project_list")  # Redirect students to projects
            elif user.role == "admin":
                return redirect("administration:admin_dashboard")
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("authentication:login")
