from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('courseupdate/', views.courseupdate,name="courseupdate"),
    path('course_form/', views.course_form,name="course_form"),
    path('coursedetails/', views.coursedetails,name="coursedetails"),
    path('eachcourse/', views.eachcourse,name="eachcourse"),
    path('eachcourseview/', views.eachcourseview,name="eachcourseview"),
    path('course_delete/', views.course_delete,name="course_delete"),
    path('coursepayment/', views.coursepayment,name="coursepayment"),
    path('paymentconfirm/', views.paymentconfirm,name="paymentconfirm"),
    path("coursevideo",views.coursevideo,name='coursevideo'),
    path('course_details', views.course_details.as_view(),name="course_details"),
    path('course_detailsview', views.course_detailsview.as_view(),name="course_detailsview"),
    path('delete_course', views.delete_course.as_view(),name="delete_course"),
    path('course_deleteview', views.course_deleteview.as_view(),name="course_deleteview"),
    path('update_course', views.update_course.as_view(),name="update_course"),
    path('course_updateview', views.course_updateview.as_view(),name="course_updateview"),
    path('payment_details', views.payment_details.as_view(),name="payment_details"),
    path('payment_detailsview', views.payment_detailsview.as_view(),name="payment_detailsview"),


]

