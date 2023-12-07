# apps/students/backends.py

from django.contrib.auth.backends import ModelBackend
from .models import StudentProfile

class StudentUserBackend(ModelBackend):
    supports_object_permissions = False

    def authenticate(self, request, username=None, password=None):
        try:
            user = StudentProfile.objects.get(username=username)
        except StudentProfile.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        else:
            return None
