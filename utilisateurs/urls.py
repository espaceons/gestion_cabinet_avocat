from django.urls import path
from utilisateurs import views

app_name = 'utilisateurs'

urlpatterns = [
    # Authentification
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('profil/', views.profile, name='profil'),
]