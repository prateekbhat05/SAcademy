from django.shortcuts import render
from student.models import *
from rest_framework.views import APIView
# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView
from adminsite.models import *
from tutor.models import *
from course.models import *
from django.http import JsonResponse


class student_create(TemplateView):
    template_name =  'student_registerdetails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = Student_register.objects.all()
        context = {"user_data": user_data}
        return context

class student_registerview(TemplateView):
    template_name =  'student_registerview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = Student_register.objects.all()
        context = {"user_data": user_data}
        return context
    
class student_updateview(TemplateView):
    template_name =  'student_updateview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = Student_register.objects.all()
        context = {"user_data": user_data}
        return context
    

class course_create(TemplateView):
    template_name =  'course_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = Student_register.objects.all()
        context = {"user_data": user_data}
        return context   




def student_createregister(request):
    return render(request,'mainadmin/student_createregister.html')

def course_form(request):
    return render(request,'course/courseform.html')

def placement(request):
    return render(request,'mainadmin/placement.html')

def mainadmin(request):
    return render(request,'mainadmin/index.html')


class SignupView(APIView):
    def post(self, request):
        name = request.POST('name')
        pnumber = request.POST('pnumber')
        email = request.POST('email')
        password = request.POST('password')

        # Create a new user record in the AdminSignup model
        new_user = Admin_signup()
        new_user.name=name
        new_user.phone_number=pnumber
        new_user.email1=email
        new_user.password=password
        new_user.save()

        return JsonResponse({'status': 'pass'})

# Class-based view to check and view admin signup details
class SignupCheckView(TemplateView):
    template_name = "view_adminsignup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userdata = Admin_signup.objects.all()
        context  = { 'userdata' : userdata}
        return context

class tutor_updateview(TemplateView):
    template_name =  'tutor_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = Employee.objects.all()
        context = {"user_data": user_data}
        return context
    
class tutor_view(TemplateView):
    template_name =  'view-tutor.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = Employee.objects.all()
        context = {"user_data": user_data}
        return context
    
class course_detailsview(TemplateView):
    
    template_name = "course-detailsview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = course_detailstable.objects.all()
        context = { 'user_data': user_data}
        return context
    
class course_deleteview(TemplateView):
    template_name =  'course-deleteview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = course_detailstable.objects.all()
        context = {"user_data": user_data}
        return context
    
class course_updateview(TemplateView):
    template_name =  'course_updateview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = course_detailstable.objects.all()
        context = {"user_data": user_data}
        return context
    
class payment_detailsview(TemplateView):
    template_name =  'payment_detailsview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = payment_detailstable.objects.all()
        context = {"user_data": user_data}
        return context
    
class jobsdetails(APIView):
    def post(self, request):
        companyname = request.POST['companyName']
        Role = request.POST['role']
        Skills = request.POST['skills']
        Salary = request.POST['salary']
        Location = request.POST['location']

        urs = job_details()
        
        urs.companyName=companyname
        urs.role=Role
        urs.skills=Skills
        urs.location=Location
        urs.salary=Salary 


        urs.save()

        return JsonResponse({'status':'pass'})
    
class job_detailsview(TemplateView):
    template_name =  'jobs_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = job_details.objects.all()
        context = {'user_data': user_data}
        return context
    

def jobportal(request):
    jobs = job_details.objects.all()  
    return render(request, 'student/job_portal.html', {'jobs': jobs})


def job_application(request):
    job_role = request.GET.get('role')
    return render(request, 'student/job-application.html', {'job_role': job_role})

class jobapplicationform(APIView):
    def post(self, request):
        jobname = request.POST['jobname']
        resume = request.FILES['resume']
        
        urs = job_applicationmodel()
        
        urs.jobname=jobname
        urs.resume=resume.name

        urs.save()

        return JsonResponse({'status':'pass'})
    
class job_applicationview(TemplateView):
    template_name =  'jobs_applicationview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = job_applicationmodel.objects.all()
        context = {'user_data': user_data}
        return context

class job_delete(TemplateView):
    template_name =  'job_deleteview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = job_details.objects.all()
        context = {"user_data": user_data}
        return context
    
class delete_job(APIView):
     def post(self, request):
        companyname = request.POST['companyname']
        job_details.objects.filter(companyName=companyname).delete()
        return JsonResponse({"status": "pass"}) 



