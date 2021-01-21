from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile, Company, Employee 

class SignUpEmployeeForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name', 'password1', 'password2']

class SignUpCompanyForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'phone']

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['logo', 'employee_num', 'description', 'category']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['user', 'jobs']
        

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class UserForm2(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']