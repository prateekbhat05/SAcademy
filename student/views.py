from django.shortcuts import render


from django.http import JsonResponse
from rest_framework.views import APIView


from student.models import Student_login
from student.models import Student_register
from course.models import *






# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request,"student/homepage.html",context=None)

def studentcourse(request):
    return render(request,"student/main-page.html",context=None)

def eachcourse(request):
    return render(request,"student/course.html",context=None)
def register(request):
    return render(request,"student/student_register.html",context=None)
def login(request):
    return render(request,"student/student_login.html",context=None)
def update(request):
    return render(request,"student/student_update.html",context=None)
def registerdetails(request):
    return render(request,"student/student_registerdetails.html",context=None)
def updatedetails(request):
    return render(request,"student/student_updatedetails.html",context=None)
def logindetails(request):
    return render(request,"student/student_logindetails.html",context=None)

def studenttoinstructor(request):
    return render(request,"student/form.html",context=None)

def dashboard(request):
    courses = course_detailstable.objects.all()  
    return render(request, 'student/dashboard.html', {'courses': courses})

def studentanalytics(request):
    return render(request,"student/student-analytics.html",context=None)



  

class student_logindetails(APIView):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['pass']
        urs = Student_login()

        urs.password = password
        urs.username = username

        urs.save()

        # print(password)
        # print(user)

        return JsonResponse({"status":"pass"})
    
class update_student(APIView):
       def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        phone_no = request.POST['phone_no']
        age = request.POST['age']
        email = request.POST['email']
        highest_qualification = request.POST['highest_qualification']
        role = request.POST['role']
        Student_register.objects.filter(phone_no = phone_no ).update(username = username,password = password, role = role, email = email, highest_qualification = highest_qualification, age = age, name = name, )

        return JsonResponse({"status":"pass"})  
    
    
from django.views.generic import TemplateView

class view_student_logindetails(TemplateView):
    template_name = "student_logindetails.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = Student_login.objects.all()
        context = { 'userdata': user_data}
        return context


class delete_student(APIView):
     def post(self, request):
        username = request.POST['username']
        Student_login.objects.filter(username=username).delete()
        return JsonResponse({"status": "pass"}) 


class student_registerdetails(APIView):
    def post(self, request):
        name = request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        age = request.POST['age']
        phone = request.POST['phone']
        mail = request.POST['mail']
        qualification = request.POST['qualification']
        role=request.POST['role']

        urs = Student_register()

        urs.age = age
        urs.name = name
        urs.phone_no = phone
        urs.username = username
        urs.password = password
        urs.role = role
        urs.email = mail
        urs.highest_qualification = qualification

        urs.save()


        return JsonResponse({"status":"pass"})
from django.views.generic import TemplateView

class view_student_registerdetails(TemplateView):
    
    template_name = "student_registerdetails.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = Student_register.objects.all()
        context = { 'user_data': user_data}
        return context

class delete_registerstudent(APIView):
     def post(self, request):
        username = request.POST['username']
        Student_register.objects.filter(username=username).delete()
        return JsonResponse({"status": "pass"}) 

class login_check(APIView):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        ent = Student_register.objects.filter(username=username,password=password).values()
        if(len(ent) > 0):
            request.session["userdata"] = ent[0]["username"]
            return JsonResponse({"status":"pass", "uid": ent[0]["sid"], "role": ent[0]["role"], "name": ent[0]["name"],"age": ent[0]["age"],"highest_qualification": ent[0]["highest_qualification"],"phone_no": ent[0]["phone_no"],"email": ent[0]["email"],"password": ent[0]["password"], "username": ent[0]["username"]})
        else:
            return JsonResponse({"status":"fail"})


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
    
class TutorCourseView(TemplateView):
    model = Student_register
    template_name = "tutor_dashboard.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.session.get("userdata")
        print("*************88")
        print(username)
        user = course_detailstable.objects.get(iname=username)
        context['coursetitle'] = user.clanguage
        return context
    
class StudentProfileView(TemplateView):
    model = Student_register
    template_name = "student-profile.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.session.get("userdata")
        user = Student_register.objects.get(username=username)
        context['currentuser'] = user.username
        context['email'] = user.email
        context['password'] = user.password
        context['phone_no']=user.phone_no

        return context
    
class StudentJobView(TemplateView):
    model = Student_register
    template_name = "student-job.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.session.get("userdata")
        user = Student_register.objects.get(username=username)
        context['currentuser'] = user.username
        context['email'] = user.email
        context['password'] = user.password
        context['phone_no']=user.phone_no

        return context
    
