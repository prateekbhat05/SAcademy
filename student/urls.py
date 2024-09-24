from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('register', views.register,name="register"),
    path('login', views.login,name="login"),
    path('update', views.update,name="update"),
    path('registerdetails', views.registerdetails,name="registerdetails"),
    path('updatedetails', views.updatedetails,name="updatedetails"),
    path('logindetails', views.logindetails,name="logindetails"),
    path('studentcourse', views.studentcourse,name="studentcourse"),
    path('studentanalytics', views.studentanalytics,name="studentanalytics"),
    path("student_logindetails", views.student_logindetails.as_view(),name="student_logindetails"),
    path('studenttoinstructor/', views.studenttoinstructor,name="studenttoinstructor"),
    path('view_student_logindetails', views.view_student_logindetails.as_view(),name="view_student_logindetails"),
    path('delete_student', views.delete_student.as_view(),name="delete_student"),
    path("student_registerdetails", views.student_registerdetails.as_view(),name="student_registerdetails"),
    path('view_student_registerdetails', views.view_student_registerdetails.as_view(),name="view_student_registerdetails"),
    path('delete_registerstudent', views.delete_registerstudent.as_view(),name="delete_registerstudent"),
    path("login_check", views.login_check.as_view(), name='login_check'),
    path("update_student", views.update_student.as_view(), name='update_student'),
    path("UserProfileView", views.UserProfileView.as_view(), name='UserProfileView'),
    path("StudentProfileView", views.StudentProfileView.as_view(), name='StudentProfileView'),
    path("StudentJobView", views.StudentJobView.as_view(), name='StudentJobView'),
    path("TutorCourseView", views.TutorCourseView.as_view(), name='TutorCourseView'),
    path("dashboard", views.dashboard, name='dashboard'),

    
]
