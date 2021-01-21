from django.urls import path
from .views import candidates_view, companies_view, home_view
urlpatterns = [
    path('', home_view, name = "index"),
    path('candidates', candidates_view, name = "candidates"),
    path('companies', companies_view, name = "companies"),
    
]    

app_name = 'home'