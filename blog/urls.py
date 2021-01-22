from django.urls import path
from .views import comment_api, like_btn, post_detail, post_list_view, post_view, add_post, update_post

urlpatterns = [
    path('', post_list_view, name = "blogs_list"),
    path('addPost', add_post, name = "add_post"),
    path('<int:id>', post_list_view, name = "blogs_category_list"),
    path('<int:id>', post_view, name = "post_detail"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/update', update_post, name='update_post'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/comment', comment_api, name = "comment"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/<int:id>/like', like_btn, name='like'),
    # path('comment/<int:id>', comment_api, name = "comment"),
    # path('<int:id>', post_category_list, name='job_details'),
    # path('addJob', add_job, name='jobEditor'),
    # path('<int:id>/like', like_btn, name='like'),
    # # path('<int:id>/dislike', disLiker, name='dislike'),
]

app_name = 'blog'