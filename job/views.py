from accounts.models import Profile, Company
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Category, Job
from .forms import  JobForm
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from .filters import JobFilter
from accounts.forms import EmployeeForm, ProfileForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
def jobs(request):

    jobs_list = Job.objects.all()
    my_filter = JobFilter(data=request.GET, queryset=jobs_list)
    jobs_list = my_filter.qs

    paginator = Paginator(jobs_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "jobs_list": page_obj,
        'my_filter': my_filter
    }
    return render(request, "job/job_list.html", context)

def job_details (request, id):

    job_details = Job.objects.get(id=id)
    if request.method == 'POST':
        return redirect(reverse('jobs:application', args=[id]))
    context = {
        "job_details": job_details,       
    }
    return render(request, "job/job_details.html", context)

@login_required
def job_apply(request, id):

    job = Job.objects.get(id=id)
    user = request.user
    profile = Profile.objects.get(user=user)
    personal_info = user.candidate
    
    profile_form = ProfileForm(instance=profile)
    personal_info_form = EmployeeForm(instance=personal_info)
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, instance=profile)
        personal_info_form = EmployeeForm(request.POST, request.FILES, instance=personal_info)
        if profile_form.is_valid() and personal_info_form.is_valid():
            form2 = profile_form.save(commit=False)
            form2.save()
            form3 = personal_info_form.save(commit=False)
            form3.save()
            form3.jobs.add(job)
            personal_info_form.save_m2m()
            messages.success(request, 'Your application has been accepted !')
            subject = f'{user.username} applied for your {job.title} job '
            message = f"{personal_info.cover_letter}"
            cv = request.FILES.getlist('cv')
            mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [job.owner.email])
            for f in cv:
                mail.attach(f.name, f.read(), f.content_type)
            mail.send()
            return redirect(reverse('jobs:job_list'))



    context = {
        "form2": profile_form,
        "form3": personal_info_form,
        'job': job
    }

    return render(request, 'job/job_application.html', context)


@login_required
def add_job(request):
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid:
            myForm = form.save(commit=False)
            myForm.owner = request.user
            myForm.save()
            return redirect(reverse("jobs:job_list"))
    else:
        form = JobForm()     

    context = {
        "jobForm": form,
    }       
    
    return render(request, "job/add_job.html", context)

def category_jobs(request, id):
    category = Category.objects.get(id=id)
    jobs = category.jobs
    my_filter = JobFilter(data=request.GET, queryset=jobs)
    jobs_list = my_filter.qs

    paginator = Paginator(jobs_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "jobs_list": page_obj,
        'my_filter': my_filter
    }
    return render(request, "job/job_list.html", context)

@login_required
def like_btn(request, id):
    
    job = Job.objects.get(id=id)

    if request.user not in job.likers.all():
        job.likers.add(request.user)
        return JsonResponse({
        'status': 'ok',
        "message": "like"
    })
    job.likers.remove(request.user)
    
    return JsonResponse({
        'status': 'ok',
        "message": "dislike"
    })
    