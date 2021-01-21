
from django.urls import path
from .views import category_jobs, job_apply, job_details, jobs, add_job, like_btn

urlpatterns = [
    path('', jobs, name = "job_list"),
    path('<int:id>', job_details, name='job_details'),
    path('addJob', add_job, name='jobEditor'),
    path('<int:id>/like', like_btn, name='like'),
    path('<int:id>/apply', job_apply, name='application'),
    path('<int:id>', category_jobs, name='category_jobs'),
]

app_name = 'job'