# organization/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import OrganizationRegistrationForm, OrganizationLoginForm
from django.contrib import messages 
from .models import ExternalOrganization
from scholarship.models import Scholarship

@login_required
def dashboard_view(request):
    organization = request.user
    organization_instance = ExternalOrganization.objects.get(account=request.user)
    scholarships_added_by_organization = Scholarship.objects.filter(added_by=organization_instance)
    context = {
        'organization': organization_instance,
        'scholarships_added_by_organization': scholarships_added_by_organization,
    }
    return render(request, 'organization/dashboard.html', context)



def register(request):
    if request.method == 'POST':
        form = OrganizationRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.user_type = "ExternalOrganization"  # Assign the user type
            user.save()
            authenticated_user = authenticate(
                request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, authenticated_user)
            return redirect('organization:registration_success')
    else:
        form = OrganizationRegistrationForm()

    organization_instance = ExternalOrganization()  # Create an instance to pass to the template
    return render(request, 'organization/register.html', {'form': form, 'organization_instance': organization_instance})



def registration_success(request):
    return render(request, 'organization/registration_success.html')

def login_view(request):
    if request.method == 'POST':
        form = OrganizationLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('organization:dashboard')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = OrganizationLoginForm()
    return render(request, 'organization/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'organization/logout.html')