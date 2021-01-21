
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.conf import settings
from taggit.managers import TaggableManager
#from .views import Company 
# Create your models here.
JOB_CHOICES = (
    ("Part Time","Part Time"),
    ("Full Time", "Full Time"),
)

# customize imges name on the file system.
def upload_job_image(instance, filename):
    extension = filename.split('.')[1]
    return 'jobs/imags/%s.%s'%(instance.title, extension)
    
        

class Job(models.Model):
    owner = models.ForeignKey(User, related_name="jobs", on_delete=models.CASCADE)
    title = models.CharField(max_length = 150)
    #description = models.TextField(max_length = 1000)
    description = RichTextField(blank=True, null=True)
    job_type = models.CharField(max_length = 150, choices=JOB_CHOICES)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=1)
    experience = models.IntegerField(default=1)
    image = models.ImageField(upload_to=upload_job_image)
    likers = models.ManyToManyField(User, related_name='liked_jobs', blank=True)
    category = models.ForeignKey('Category', related_name='jobs', on_delete=models.SET_NULL, null=True)
    objects = models.Manager()
    skills = TaggableManager()

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.title


class Category(models.Model):
    """Model definition for MODELNAME."""

    name = models.CharField(max_length = 150)

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.name

       





    
    

    
            
    
    

    