from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Credential

# Registration view
def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect if the user is already logged in

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'credentials/register.html', {'form': form})

# Login view
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect if user is already logged in

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}! You are now logged in.')
                next_url = request.GET.get('next', 'dashboard')  # Redirect to 'next' URL if available
                return redirect(next_url)
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'credentials/login.html', {'form': form})

# Logout view
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have been logged out.')
    return redirect('login')

# Dashboard view showing the user's credentials
@login_required
def dashboard_view(request):
    credentials = Credential.objects.filter(user=request.user)
    if not credentials:
        messages.info(request, "You have no credentials saved.")
    return render(request, 'credentials/dashboard.html', {'credentials': credentials})
