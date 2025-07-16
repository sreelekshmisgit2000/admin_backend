from django.contrib import admin
from .models import Doctor, Education, Certification, SpecializationIcon

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class CertificationInline(admin.TabularInline):
    model = Certification
    extra = 1

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialization', 'experience_years', 'is_active']
    search_fields = ['name', 'specialization__name']
    inlines = [EducationInline, CertificationInline]

admin.site.register(SpecializationIcon)
