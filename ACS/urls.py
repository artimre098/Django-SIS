from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('acs',views.acs ,name='acs'),
    path('register/',views.register ,name='register'),
]
