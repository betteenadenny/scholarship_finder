# student/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import StudentRegistrationForm, StudentLoginForm,StudentUpdateForm
from django.contrib import messages 
from .models import StudentProfile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

def dashboard_view(request):
    student = StudentProfile.objects.get(username=request.user.username)
    valid_scholarships = student.get_valid_scholarships()
    context = {
        'student': student,
        'valid_scholarships': valid_scholarships,
    }
    print("Context:", context)
    return render(request, 'student/dashboard.html', context)

@login_required
def update_profile(request):
    student = StudentProfile.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student:dashboard')
    else:
        form = StudentUpdateForm(instance=student)
    return render(request, 'student/update_profile.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            account = User.objects.create(username = form.cleaned_data['username'],password = make_password(form.cleaned_data['password1']))
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.user_type = 'student'
            authenticated_user = authenticate(
                request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            user.account = account
            user.save()
            login(request, authenticated_user)
            return redirect('student:registration_success') 
    else:
        form = StudentRegistrationForm()

    return render(request, 'student/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('student:dashboard')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = StudentLoginForm()
    return render(request, 'student/login.html', {'form': form})

def registration_success(request):
    return render(request, 'student/registration_success.html')
