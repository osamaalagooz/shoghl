
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from django.conf import settings
from taggit.managers import TaggableManager
from job.models import Category, Job 


# Create your models here.
def upload_company_image(instance, filename):
    extension = filename.split('.')[1]
    return 'companies/logos/%s.%s'%(instance.id, extension)
   
def upload_cv(instance, filename):
    extension = filename.split('.')[1]
    return 'candidaties/cvs/%s.%s'%(instance.id, extension)

def upload_image(instance, filename):
    extension = filename.split('.')[1]
    return 'candidaties/images/%s.%s'%(instance.id, extension)


class Profile(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length = 15)
    city = models.ForeignKey("City", on_delete=models.CASCADE, null=True, related_name='user_profile')
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)    

class City(models.Model):
    name = models.CharField(max_length = 50) 

    def __str__(self):
        return self.name
    
class Company(models.Model):
    logo = models.ImageField(upload_to=upload_company_image, null=True, blank=True)
    employee_num = models.IntegerField(default=0)
    description = RichTextField(blank=True, null=True)
    user =  models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.user.first_name

class Employee(models.Model):
    job_title = models.CharField(max_length = 13)
    bio = models.TextField(max_length=500)
    user =  models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate')
    image = models.ImageField(upload_to=upload_image, null=True, blank=True)
    website = models.URLField(max_length = 300)
    cv = models.FileField(upload_to=upload_cv, null=True, blank=True)
    summary = RichTextField(blank=True, null=True)
    jobs = models.ManyToManyField(Job, related_name='candidaties', blank=True)
    objects = models.Manager()
    skills = TaggableManager()
    def __str__(self):
        return self.user.username
    
    