from django.shortcuts import render,get_object_or_404

# Create your views here.]
from django.http import HttpResponse
from rest_framework.views import APIView
from django.http import JsonResponse
from django.views.generic import TemplateView
from .models import *
from student.models import *
from course.models import *



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def interviewRegister(request):
    return render(request,"tutor/interviewer-register.html")
def login(request):
    return render(request,"tutor/login.html")
def tutor(request):
    return render(request,"tutor/tutor.html")

class tutor_dashboard(TemplateView):
    template_name = "tutor/tutor_dashboard.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.session.get("userdata")
        print("*************88")
        print(username)
        user = course_detailstable.objects.filter(iname = username)
        print(user)
        context['courses'] = user
        return context
    
class create_user(APIView):
    def post(self, request):
        print(request.POST)
        role = request.POST['role']
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        skills = request.POST['skills']
       
        
        usr = Employee()
        usr.role = role
        usr.name = name
        usr.email = email
        usr.password = password
        usr.phone = phone
        usr.skills = skills
       
        usr.save()
        return JsonResponse({"status" : "pass"})
    
class view_user(TemplateView):
    
    template_name = "tutorregister.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = Employee.objects.all()
        context = { 'userdata': user_data}
        return context

class deleteuser(APIView):
    def post(self, request):
        name = request.POST['name']
        Employee.objects.filter(name = name).delete()
        return JsonResponse({"status": "pass"})
    

class UserProfileView(TemplateView):
    model = Student_register
    template_name = "profile.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.session.get("userdata")
        user = Student_register.objects.get(username=username)
        context['currentuser'] = user.username
        context['email'] = user.email
        context['password'] = user.password
        context['phone_no']=user.phone_no
        return context