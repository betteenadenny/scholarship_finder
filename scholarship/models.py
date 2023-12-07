from django.db import models
from organization.models import ExternalOrganization

class Scholarship(models.Model):
    SCHOLARSHIP_TYPES = [
        ('Private', 'Private'),
        ('Government', 'Government'),
        ('Central Government', 'Central Government'),
    ]

    SCHOLARSHIP_CATEGORIES = [
        ('Sports', 'Sports'),
        ('Academics', 'Academics'),
        ('Other', 'Other'),
    ]

    DEGREE_TYPES = [
        ('Undergraduate', 'Undergraduate'),
        ('Postgraduate', 'Postgraduate'),
        ('PhD/Doctorate', 'PhD/Doctorate'),
        ('Diploma', 'Diploma'),
        ('Other', 'Other'),
    ]

    MAJOR_CHOICES = [
        ('Engineering', 'Engineering'),
        ('Science', 'Science'),
        ('Arts', 'Arts'),
        ('Computer Science', 'Computer Science'),
        ('Other', 'Other'),
    ]

    INCOME_CHOICES = [
        ('Less than 100000', 'Less than 100000'),
        ('Less than 500000', '100000 - 500000'),
        ('Less than 1000000', '500000 - 1000000'),
        ('Less than 1000000', 'More than 1000000'),
        ('Not applicable','Not applicable'),

    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=SCHOLARSHIP_TYPES)
    category = models.CharField(max_length=20, choices=SCHOLARSHIP_CATEGORIES)
    description = models.TextField()
    application_start_date = models.DateField()
    application_end_date = models.DateField()
    annual_income = models.CharField(max_length=20,choices= INCOME_CHOICES, help_text="Family Annuval income range of the applicant")
    degree_types = models.CharField(max_length=20, choices=DEGREE_TYPES, help_text="Types of degrees eligible for the scholarship")
    major = models.CharField(max_length=20, choices=MAJOR_CHOICES)
    application_link = models.URLField(help_text="Link to the scholarship application")
    added_by = models.ForeignKey(ExternalOrganization, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False, help_text="Verification status of the scholarship")

    def __str__(self):
        return self.name
