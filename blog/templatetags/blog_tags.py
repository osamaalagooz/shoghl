from ..models import Post
from django import template
import datetime
import timeago
from django.utils import timezone

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()

@register.inclusion_tag('recent_posts.html/')
def show_recent_posts(count=5):
    recent_posts = Post.published.order_by('-publish')[:count]
    return {'recent_posts': recent_posts}

@register.filter
def time_ago(val):
    now = timezone.now()
    return timeago.format(val, now)