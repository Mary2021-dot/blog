from django.urls import path
from . import views
app_name = 'users'


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('upload/', views.upload, name='upload'),
     path('logout/', views.login, name='logout'),
    path('profile/', views.profile, name='profiile'),
    
]