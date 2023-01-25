from django.urls import path
from . import views

app_name = "login"

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('', views.direct, name='direct'),
    path('logout/', views.login, name='logout')
]
