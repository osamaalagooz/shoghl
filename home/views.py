from django.core.paginator import Paginator
from job.filters import JobFilter
from django.shortcuts import render
from job.models import Job, Category 
from accounts.models import Employee, Company


# Create your views here.
def home_view(request):
    jobs = Job.objects.all()[:10]
    categories = Category.objects.all()
    candidaties = Employee.objects.all()
    companies = Company.objects.all()



    print(jobs)
    context = {
        "jobs": jobs,
        "categories": categories,
        "candidaties": candidaties,
        "companies": companies
    }
    return render(request, 'home.html', context)

def candidates_view(request):
    candidates = Employee.objects.all()

    return render(request,"candidate.html",{"candidates": candidates})


def companies_view(request):
    companies = Company.objects.all()

    return render(request,"companies.html",{"companies": companies})
# def category_jobs(request, id):
#     category = Category.objects.get(id=id)
#     jobs = category.jobs
#     my_filter = JobFilter(data=request.GET, queryset=jobs)
#     jobs_list = my_filter.qs

#     paginator = Paginator(jobs_list, 5)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         "jobs_list": page_obj,
#         'my_filter': my_filter
#     }
#     return render(request, "job/job_list.html", context)