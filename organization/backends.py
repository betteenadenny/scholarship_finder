# apps/organizations/backends.py

from django.contrib.auth.backends import ModelBackend
from .models import ExternalOrganization

class OrganizationUserBackend(ModelBackend):
    supports_object_permissions = False

    def authenticate(self, request, username=None, password=None):
        try:
            user = ExternalOrganization.objects.get(username=username)
        except ExternalOrganization.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        else:
            return None
