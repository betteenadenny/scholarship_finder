from django.contrib.auth.models import AbstractUser
from django.db import models
from  scholarship.models import Scholarship
from django.contrib.auth.hashers import make_password
from organization.models import ExternalOrganization
from django.contrib.auth.models import User

class StudentProfile(AbstractUser):
    account = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    type = models.CharField(max_length=20, choices=Scholarship.SCHOLARSHIP_TYPES,help_text=" the types of scholarships you are interested in.")
    category = models.CharField(max_length=20, choices=Scholarship.SCHOLARSHIP_CATEGORIES)
    annual_income = models.CharField(max_length=20, choices=Scholarship.INCOME_CHOICES)
    degree_type = models.CharField(max_length=20, choices=Scholarship.DEGREE_TYPES,help_text="Current degree you are pursuing ")
    major = models.CharField(max_length=20, choices=Scholarship.MAJOR_CHOICES)


    def get_valid_scholarships(self):
        valid_scholarships = Scholarship.objects.filter(
            type=self.type,
            category=self.category,
            major=self.major,
            annual_income=self.annual_income,
            degree_types=self.degree_type,
        )
        return valid_scholarships
    
    
    def save(self, *args, **kwargs):
        # Check if the password is not set or explicitly requested to be regenerated
        if not self.password or kwargs.get('regenerate_password', False):
            self.password = make_password(None)  # Generate a random password

        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    class Meta:
        permissions = [
            ('can_add_student', 'Can add Student'),
        ]

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='student_groups',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='student_user_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
        related_query_name='student_user',
    )