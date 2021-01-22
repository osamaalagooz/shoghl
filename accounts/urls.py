from django.urls import path
from .views import candidate_profile, profile, edit_company_profile,edit_candidate_profile, sign_up_candidate, sign_up_company,company_profile

urlpatterns = [
    path('signup/candidate',sign_up_candidate , name = "sign_up_candidate"),
    path('signup/company',sign_up_company , name = "sign_up_company"),
    path('profile/', profile , name = "login_profile"),
    path('companies/profile/<int:id>',company_profile , name = "profile"),
    path('candidates/profile/<int:id>',candidate_profile , name = "candidate_profile"),
    path('companies/profile/<int:id>/edit', edit_company_profile, name = "profile_editor"),
    path('candidates/profile/<int:id>/edit', edit_candidate_profile, name = "candidate_profile_editor"),
]

app_name = 'accounts'