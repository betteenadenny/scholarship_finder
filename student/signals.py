# student/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import StudentProfile

@receiver(post_save, sender=User)
def create_or_save_student_profile(sender, instance, created, **kwargs):
    if hasattr(instance, 'student'):
        if created:
            StudentProfile.objects.create(user=instance)
        instance.student.save()
    else:
        StudentProfile.objects.create(user=instance)