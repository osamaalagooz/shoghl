from django.contrib import admin

# Register your models here.
from .models import Company, Profile, City, Employee

admin.site.register(Profile)
admin.site.register(City)
admin.site.register(Employee)
admin.site.register(Company)