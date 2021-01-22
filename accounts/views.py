from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignUpCompanyForm, SignUpEmployeeForm, ProfileForm, UserForm, CompanyForm, EmployeeForm
from django.contrib.auth import authenticate, login
from .models import Company, Profile, Employee
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User


# Create your views here.
def sign_up_candidate(request):


    if request.method == "POST":
        form1 = SignUpEmployeeForm(request.POST)
        form2 = EmployeeForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            print('valid')
            form1.save()
            username = form1.cleaned_data.get('username')
            password = form1.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                candidate_form = form2.save(commit=False)
                candidate_form.user = request.user
                candidate_form.save()
                form2.save_m2m()
                messages.success(request, 'Your have been successfully registered !')
                return redirect(reverse("register:candidate_profile", args=[user.id]))

            else:

                return HttpResponse('there something wrong !')
    else:
        form1 = SignUpEmployeeForm()
        form2 = EmployeeForm()

    context = {
        'form1': form1,
        "form2":form2
    }

    return render(request, 'registration/signup.html', context)

def sign_up_company(request):

    if request.method == "POST":

        form1 = SignUpCompanyForm(request.POST)
        form2 = CompanyForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            username = form1.cleaned_data.get('username')
            password = form1.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user:
                    login(request, user)
                    company_form = form2.save(commit=False)
                    company_form.user = request.user
                    company_form.save()
                    messages.success(request, 'Your have been successfully registered !')
                    return redirect(reverse('register:profile', args=[user.id]))

            else:

                    return HttpResponse('there something wrong !')
    else:
        form1 = SignUpCompanyForm()
        form2 = CompanyForm()

    context = {
        'form1': form1,
        "form2": form2
    }

    return render(request, 'registration/signup.html', context)
def profile(request):
    user = request.user
    try:
        if user.candidate != None :
            return redirect(reverse("register:candidate_profile", args=[user.id]))
    except:
        return redirect(reverse("register:profile", args=[user.id]))

    #elif user.company != None:
       # return redirect(reverse("register:profile", args=[user.id]))
    #else:
        #return redirect(reverse("home:index"))

def company_profile(request, id):

    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    return render(request, 'accounts/profile.html', {'profile': profile})

def candidate_profile(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    return render(request, 'accounts/candidate_profile.html', {'profile': profile})



def edit_company_profile(request, id):

    profile = Profile.objects.get(user=request.user)
    company = Company.objects.get(user=request.user)
    if request.method == "POST":
        profileform = ProfileForm(request.POST,request.FILES, instance=profile)
        userform = UserForm(request.POST, instance=request.user )
        companyform = CompanyForm(request.POST,request.FILES, instance=company)
        if profileform.is_valid() and userform.is_valid():
            userform.save()
            my_profileform = profileform.save(commit=False)
            my_profileform.user = request.user
            my_profileform.save()
            my_companyform = companyform.save(commit=False)
            my_companyform.user = request.user
            my_companyform.save()
            return redirect(reverse('register:profile', args=[request.user.id]))
    else:
        profileform = ProfileForm(instance=profile)
        userform = UserForm(instance=request.user)
        companyform = CompanyForm(instance=company)

    context = {
        'profileform': profileform,
        'userform': userform,
        'companyform': companyform
    }
    return render(request, 'accounts/profile_edit.html', context)

def edit_candidate_profile(request, id):

    profile = Profile.objects.get(user=request.user)
    candidate = Employee.objects.get(user=request.user)
    if request.method == "POST":
        profileform = ProfileForm(request.POST,request.FILES, instance=profile)
        userform = UserForm(request.POST, instance=request.user )
        candidateform = EmployeeForm(request.POST,request.FILES, instance=candidate)
        if profileform.is_valid() and userform.is_valid():
            userform.save()
            my_profileform = profileform.save(commit=False)
            my_profileform.user = request.user
            my_profileform.save()
            my_candidateform = candidateform.save(commit=False)
            my_candidateform.user = request.user
            my_candidateform.save()
            return redirect(reverse('register:candidate_profile', args=[request.user.id]))
    else:
        profileform = ProfileForm(instance=profile)
        userform = UserForm(instance=request.user)
        candidateform = EmployeeForm(instance=candidate)

    context = {
        'profileform': profileform,
        'userform': userform,
        'candidateform': candidateform
    }
    return render(request, 'accounts/candidate_profile_edit.html', context)