# Generated by Django 5.1.5 on 2025-07-16 09:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('qualification', models.CharField(max_length=100)),
                ('experience_years', models.PositiveIntegerField()),
                ('contact_number', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('is_active', models.BooleanField(default=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='doctors/')),
                ('bio', models.TextField(blank=True)),
                ('clinic_address', models.TextField(blank=True)),
                ('available_days', models.CharField(blank=True, max_length=100)),
                ('available_time_start', models.TimeField(blank=True, null=True)),
                ('available_time_end', models.TimeField(blank=True, null=True)),
                ('rating', models.FloatField(default=0.0)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpecializationIcon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='specialization_icons/')),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('issued_by', models.CharField(max_length=150)),
                ('issue_date', models.DateField()),
                ('certificate_file', models.FileField(blank=True, null=True, upload_to='certificates/')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certifications', to='doctors_app.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=150)),
                ('year', models.PositiveIntegerField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='doctors_app.doctor')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctors_app.specializationicon'),
        ),
    ]
