from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class ExternalOrganization(AbstractUser):
    account = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    website = models.URLField()
    file_title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/', blank=True)
    is_verified = models.BooleanField(default=False) 

    def save(self, *args, **kwargs):
        if not self.password or kwargs.get('regenerate_password', False):
            self.password = make_password(None)  
        super().save(*args, **kwargs)
    def __str__(self):
        return self.username
    class Meta:
        permissions = [
            ('can_add_organization', 'Can add organization'),
        ]
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='organization_groups',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='organization_user_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
        related_query_name='organization_user',
    )
