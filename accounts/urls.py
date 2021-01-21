from django.urls import path
from .views import candidate_profile, profile, edit_profile, sign_up_candidate, sign_up_company

urlpatterns = [
    path('signup/candidate',sign_up_candidate , name = "sign_up_candidate"),
    path('signup/company',sign_up_company , name = "sign_up_company"),
    path('profile/',profile , name = "profile"),
    path('profile/<int:id>',candidate_profile , name = "candidate_profile"),
    path('profile/edit', edit_profile, name = "profile_editor"),
] 

app_name = 'accounts'