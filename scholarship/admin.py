from django.contrib import admin
from .models import Scholarship
from .forms import AdminScholarshipForm

class ScholarshipAdmin(admin.ModelAdmin):
    form = AdminScholarshipForm
    filter_horizontal = ('major',)  # Adjust as needed

admin.site.register(Scholarship)
