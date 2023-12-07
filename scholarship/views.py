from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from organization.models import ExternalOrganization 
from .forms import ScholarshipForm,UpdateScholarshipForm
from .models import Scholarship
from django.contrib.auth import get_user_model
from django.contrib import messages
 
User = get_user_model()

def home(request):
  return render(request,'scholarship/home.html')

@login_required
def scholarship_form(request):
    if request.method == 'POST':
        form = ScholarshipForm(request.POST)
        if form.is_valid():
            scholarship = form.save(commit=False)
            
            # Ensure the added_by field is an ExternalOrganization instance
            if isinstance(request.user, ExternalOrganization):
                scholarship.added_by = request.user
            else:
                error_message = 'Invalid user type'
                print(error_message)

            scholarship.save()
            return redirect('scholarship:success_page')  # Redirect to a success page
    else:
        form = ScholarshipForm()

    return render(request, 'scholarship/scholarship_form.html', {'form': form})


def success_view(request):
    return render(request, 'scholarship/success_page.html')

@login_required
def update_scholarship(request,scholarship_id):
    scholarship = Scholarship.objects.get(id=scholarship_id,added_by=request.user.externalorganization)
    if request.method == 'POST':
        form = UpdateScholarshipForm(request.POST, instance=scholarship)
        if form.is_valid():
            form.save()
            messages.success(request, 'Scholarship has been updated successfully.')
            return redirect('organization:dashboard')
    else:
        form = UpdateScholarshipForm(instance=scholarship)
    return render(request, 'scholarship/update_scholarship.html', {'form': form})






    