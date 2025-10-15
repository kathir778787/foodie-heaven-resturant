from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User

# -------------------- USER VIEWS --------------------

def main(request):
    return render(request, 'main.html')
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect('main')




def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')
def forgotpassword(request):
    return render(request,'forgotpassword.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')

    return render(request, 'register.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def dishes(request):
    return render(request, 'dishes.html')


def ourdishes(request):
    return render(request, 'ourdishes.html')


def reservation(request):
    return render(request, 'reservation.html')


def policy(request):
    return render(request, 'policy.html')


def terms(request):
    return render(request, 'terms.html')


def index(request):
    return render(request, 'index.html')


# -------------------- ADMIN VIEWS --------------------

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        if username == 'admin' and password == 'admin123':  # Example check
            request.session['admin'] = True
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Invalid admin credentials")
    
    return render(request, 'admin_login.html')


def admin_dashboard(request):
    if not request.session.get('admin'):
        return redirect('admin_login')
    return render(request, 'admin-dashboard.html')


def admin_contact(request):
    if not request.session.get('admin'):
        return redirect('admin_login')
    return render(request, 'admin-contact.html')


def admin_dishes(request):
    if not request.session.get('admin'):
        return redirect('admin_login')
    return render(request, 'admin-dishes.html')


def admin_reservation(request):
    if not request.session.get('admin'):
        return redirect('admin_login')
    return render(request, 'admin-reservation.html')

