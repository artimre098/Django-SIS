from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('acs',views.acs ,name='acs'),
    path('resume',views.resume ,name='resume'),
    path('register/',views.register ,name='register'),
    path('logout/',views.logout_user, name='logout'),
    path('students/<int:pk>',views.student_record, name='students'),
    path('edit-record/<int:pk>',views.update_record, name='update_student'),
]
