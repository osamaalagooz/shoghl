from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.utils.text import slugify 

# Create your models here.
User = settings.AUTH_USER_MODEL

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

def upload_post_image(instance, filename):
    extension = filename.split('.')[1]
    if instance.title:
        return '%s.%s'%(instance.title, extension)
    else:
        return 'posts/imags/%s.%s'%(instance.name, extension)




class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
      return self.title

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to=upload_post_image)
    body = RichTextField(blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager
    tags = TaggableManager()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    likers = models.ManyToManyField(User, related_name='liked_posts', blank=True)


    class Meta:
        ordering = ('-publish',)

    def __str__(self):
       return self.title

    def get_absolute_url(self):
        return reverse('blogs:post_detail',
        args=[self.publish.year,
        self.publish.month,
        self.publish.day, self.slug])  
         
    def save(self, *args, **kwargs): 
        self.slug = slugify(self.title) 
        super(Post, self).save(*args, **kwargs) 

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    commenter = models.ForeignKey(User, related_name='blog_posts',on_delete=models.CASCADE) 
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
      ordering = ('created',)

    def __str__(self):
      return f'Comment by {self.commenter.username} on {self.post.title}'

class CommentReply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_replys')
    comment_replier =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='repliers')   
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
      return f'Reply by {self.comment_replier.username} on {self.comment.body}'

