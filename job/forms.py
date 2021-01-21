from django import forms 
from .models import  Job

# class EmployeeForm(forms.ModelForm):

#     class Meta:
#        model = Employee
#        fields = ["name", "email", "website", "cv", "cover_letter"]

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"       
        exclude = ("owner",'likers', 'likes_num')
        
