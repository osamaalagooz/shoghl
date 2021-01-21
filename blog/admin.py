from django.contrib import admin
from .models import Comment, CommentReply, Post, Category
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #list_display = ('title', 'slug', 'author', 'publish', 'status', 'post_comments')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('commenter', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('commenter','body')


@admin.register(CommentReply)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_replier', 'comment','created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('body','replier')

admin.site.register(Category)