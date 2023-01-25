from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #for showing img in html

app_name = "lesson"

urlpatterns = [
    path('insert/', views.insert, name='insert')
]

urlpatterns += staticfiles_urlpatterns() #for showing img in html
