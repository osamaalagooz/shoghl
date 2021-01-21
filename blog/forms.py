from django import forms
from django.db.models import fields
from .models import Post, Comment, CommentReply

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'image', 'body', 'status', 'category']
        
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']      

class CommentReplyForm(forms.ModelForm):

    class Meta:
        model = CommentReply
        fields = ['body']              