from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('interviewRegister/', views.interviewRegister,name="interviewRegister"),
    path('login/', views.tutor,name="login"),
    path('tutor/', views.tutor,name="tutor"),
    path('tutor_dashboard/', views.tutor_dashboard.as_view(),name="tutor_dashboard"),
    path("create_user", views.create_user.as_view(),name="create_user"),
    path("view_user", views.view_user.as_view(),name="view_user"),
    path("deleteuser", views.deleteuser.as_view(),name="deleteuser"),
    path("UserProfileView", views.UserProfileView.as_view(),name="UserProfileView"),

    

]
