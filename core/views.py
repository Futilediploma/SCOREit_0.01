from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from leagues.models import League
from datetime import datetime

def home(request):
    return render(request, 'core/home.html', {'year': datetime.now().year})

def pricing(request):
    return render(request, 'core/pricing.html')

def features(request):
    return render(request, 'core/features.html')  

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # ✅ fixed typo
        if form.is_valid():  # ✅ fixed typo
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})  # ✅ fixed typo

def about(request):
    return render(request, 'core/about.html')

def custom_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')  
 
@login_required
def dashboard(request):
    leagues = League.objects.filter(created_by=request.user)
    return render(request, 'core/dashboard.html', {'leagues': leagues})
