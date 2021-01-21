from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignUpCompanyForm, SignUpEmployeeForm, ProfileForm, UserForm, CompanyForm, EmployeeForm
from django.contrib.auth import authenticate, login
from .models import Company, Profile
from django.contrib import messages
from django.urls import reverse


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
                return redirect(reverse("register:profile"))

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
                    company_form.user = user
                    company_form.save()
                    messages.success(request, 'Your have been successfully registered !')
                    return redirect(reverse("register:profile"))

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

    profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})

def candidate_profile(request, id):
    profile = Profile.objects.get(id=id)
    return render(request, 'accounts/candidate_profile.html', {'profile': profile})
 


def edit_profile(request):
    
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        profileform = ProfileForm(request.POST,request.FILES, instance=profile)
        userform = UserForm(request.POST, instance=request.user )
        if profileform.is_valid() and userform.is_valid():
            userform.save()
            my_profileform = profileform.save(commit=False) 
            my_profileform.user = request.user
            my_profileform.save()
            return redirect('/accounts/profile')
    else:
        profileform = ProfileForm(instance=profile)
        userform = UserForm(instance=request.user)

    context = {
        'profileform': profileform,
        'userform': userform,
    }
    return render(request, 'accounts/profile_edit.html', context)