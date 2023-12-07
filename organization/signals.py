# organization/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import ExternalOrganization

@receiver(post_save, sender=User)
def create_or_update_organization_profile(sender, instance, created, **kwargs):
    # Check if the user has an associated external organization
    if hasattr(instance, 'externalorganization'):
        # If the user doesn't have an external organization, create one
        if created:
            ExternalOrganization.objects.create(user=instance)
        # Save the external organization
        instance.externalorganization.save()
    else:
        # If the user doesn't have the externalorganization attribute, create and save it
        ExternalOrganization.objects.create(user=instance)

