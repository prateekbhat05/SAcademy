from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path("",views.mainadmin,name='mainadmin'),
    path("student_create",views.student_create.as_view(),name='student_create'),
    path("student_registerview",views.student_registerview.as_view(),name='student_registerview'),
    path("student_createregister",views.student_createregister,name='student_createregister'),
    path("placement",views.placement,name='placement'),
    path("jobportal",views.jobportal,name='jobportal'),
    path("job_application",views.job_application,name='job_application'),
    path("signup_view",views.SignupView.as_view(),name='signup_view'),
    path("student_updateview",views.student_updateview.as_view(),name='student_updateview'),
    path("course_create",views.course_create.as_view(),name='course_create'),
    path("tutor_updateview",views.tutor_updateview.as_view(),name='tutor_updateview'),
    path("tutor_view",views.tutor_view.as_view(),name='tutor_view'),
    path("course_form",views.course_form,name='course_form'),
    path("payment_detailsview",views.payment_detailsview.as_view(),name='payment_detailsview'),
    path("jobsdetails",views.jobsdetails.as_view(),name='jobsdetails'),
    path("job_detailsview",views.job_detailsview.as_view(),name='job_detailsview'),
    path("jobapplicationform",views.jobapplicationform.as_view(),name='jobapplicationform'),
    path("job_applicationview",views.job_applicationview.as_view(),name='job_applicationview'),
    path("job_delete",views.job_delete.as_view(),name='job_delete'),
    path("delete_job",views.delete_job.as_view(),name='delete_job'),



    # path("student_create",views.student_create,name='student_create')
]


