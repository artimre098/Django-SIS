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
    path('delete-record/<int:pk>',views.delete_record, name='delete_student'),
    path('add-account/',views.add_account ,name='add_account'),
]
