# Generated by Django 4.2.7 on 2023-12-02 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('Private', 'Private'), ('Government', 'Government'), ('Central Government', 'Central Government')], max_length=20)),
                ('category', models.CharField(choices=[('Sports', 'Sports'), ('Academics', 'Academics'), ('Other', 'Other')], max_length=20)),
                ('description', models.TextField()),
                ('application_start_date', models.DateField()),
                ('application_end_date', models.DateField()),
                ('annual_income', models.CharField(choices=[('Less than 100000', 'Less than 100000'), ('Less than 500000', '100000 - 500000'), ('Less than 1000000', '500000 - 1000000'), ('Less than 1000000', 'More than 1000000'), ('Not applicable', 'Not applicable')], help_text='Family Annuval income range of the applicant', max_length=20)),
                ('degree_types', models.CharField(choices=[('Undergraduate', 'Undergraduate'), ('Postgraduate', 'Postgraduate'), ('PhD/Doctorate', 'PhD/Doctorate'), ('Diploma', 'Diploma'), ('Other', 'Other')], help_text='Types of degrees eligible for the scholarship', max_length=20)),
                ('majors', models.CharField(choices=[('Engineering', 'Engineering'), ('Science', 'Science'), ('Arts', 'Arts'), ('Computer Science', 'Computer Science'), ('Other', 'Other')], max_length=20)),
                ('application_link', models.URLField(help_text='Link to the scholarship application')),
                ('verified', models.BooleanField(default=False, help_text='Verification status of the scholarship')),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.externalorganization')),
            ],
        ),
    ]
