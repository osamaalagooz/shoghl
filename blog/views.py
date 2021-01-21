import json
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Post, Comment, Category, CommentReply
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from .forms import CommentForm, CommentReplyForm


# Create your views here.

def post_list_view(request, id=None):
    
    if id:
        category = Category.objects.get(id=id)
        posts = category.posts.all()
        
    else:    
        posts =  Post.published.all()

    categories = Category.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)  
    except EmptyPage:
        posts  = paginator.page(paginator.num_pages)     

    return render(request, 'posts_list.html', {'posts': posts, 'categories': categories})


def post_view(request, id):
    
    post = Post.objects.get(id=id)
    return render(request, 'post_view.html', {'post':post})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    comments = post.post_comments.filter(active=True)
    reply_form = CommentReplyForm()
    post_tags_ids = post.tags.values_list('id', flat=True)
    post_tags_names = post.tags.values_list('name', flat=True).all()   
    print(post_tags_names.all())
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
           

    return render(request, 'post_view.html',{'post': post,
                                                     'comments': comments,
                                                     'reply_form': reply_form,
                                                     'similar_posts': similar_posts,
                                                     'tags': post_tags_names}
                                                     )        
@login_required
def comment_api(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    
    if request.body:
        print(request.body)
        data = json.loads(request.body.decode("utf-8"))
        body = data.get('body')
        Comment.objects.create(commenter=request.user, body=body, post=post)
        return JsonResponse({
            'message': "the comment submitted"
        })

@login_required
def like_btn(request, year, month, day, post,id):
    
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)

    if request.user not in post.likers.all():
        post.likers.add(request.user)
        return JsonResponse({
        'status': 'ok',
        "message": "like"
    })
    post.likers.remove(request.user)
    
    return JsonResponse({
        'status': 'ok',
        "message": "dislike"
    })