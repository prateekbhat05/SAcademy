from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.views import APIView
from django.http import JsonResponse
from django.views.generic import TemplateView
from course.models import *


def index(request):
    return render(request,"course/courseform.html",context=None)

def course_form(request):
    return render(request,"course/courseform.html",context=None)

def courseupdate(request):
    return render(request,"course/courseformUpdate.html",context=None)

def coursedetails(request):
    return render(request,"course/courseDetails.html",context=None)

def coursepayment(request):
    course_id = request.GET.get('id')
    course = course_detailstable.objects.get(ctitle=course_id)  
    return render(request, 'course/payment.html', {'course': course})

def paymentconfirm(request):
    course_id = request.GET.get('id')
    course = course_detailstable.objects.get(ctitle=course_id)  
    return render(request, 'course/paymentconfirm.html', {'course': course})
    
def eachcourse(request):
    course_id = request.GET.get('id')
    course = course_detailstable.objects.get(ctitle=course_id)  
    return render(request, 'course/course.html', {'course': course})

def eachcourseview(request):
    course_id = request.GET.get('id')
    course = course_detailstable.objects.get(ctitle=course_id)  
    return render(request, 'course/course_viewonly.html', {'course': course})

def course_delete(request):
    return render(request,"course/course-deleteview.html",context=None)

class course_details(APIView):
    def post(self, request):
        ctitle = request.POST['ctitle']
        clanguage=request.POST['clanguage']
        iname=request.POST['iname']
        clevel = request.POST['clevel']
        ctime = request.POST['ctime']
        cdetails = request.POST['cdetails']
        ccost = request.POST['ccost']

        crs = course_detailstable()

        crs.ctitle=ctitle
        crs.clanguage=clanguage
        crs.iname=iname
        crs.clevel=clevel
        crs.ctime=ctime
        crs.cdetails=cdetails
        crs.ccost=ccost

        crs.save()

        return JsonResponse({"status":"pass"})

class course_detailsview(TemplateView):
    
    template_name = "course-detailsview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = course_detailstable.objects.all()
        context = { 'user_data': user_data}
        return context

class delete_course(APIView):
     def post(self, request):
        ctitle = request.POST['ctitle']
        course_detailstable.objects.filter(ctitle=ctitle).delete()
        return JsonResponse({"status": "pass"})
     

class course_deleteview(TemplateView):
    template_name =  'course-deleteview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = course_detailstable.objects.all()
        context = {"user_data": user_data}
        return context
    
class update_course(APIView):
       def post(self, request):
        ctitle = request.POST['ctitle']
        clanguage = request.POST['clanguage']
        iname = request.POST['iname']
        clevel = request.POST['clevel']
        ctime = request.POST['ctime']
        cdetails = request.POST['cdetails']
        ccost = request.POST['ccost']
        course_detailstable.objects.filter(ctitle = ctitle ).update(clanguage = clanguage,iname = iname, clevel = clevel, ctime = ctime, cdetails = cdetails, ccost = ccost, )

        return JsonResponse({"status":"pass"}) 
       
class course_updateview(TemplateView):
    template_name =  'course_updateview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = course_detailstable.objects.all()
        context = {"user_data": user_data}
        return context
    
class payment_details(APIView):
    def post(self, request):
        cardtype = request.POST['cardtype']
        cardholdername=request.POST['cardholdername']
        cardnumber=request.POST['cardnumber']
        expirydate = request.POST['expirydate']
        cvv = request.POST['cvv']

        crs = payment_detailstable()

        crs.cardtype=cardtype
        crs.cardholdername=cardholdername
        crs.cardnumber=cardnumber
        crs.expirydate=expirydate
        crs.cvv=cvv

        crs.save()

        return JsonResponse({"status":"pass"})
    
class payment_detailsview(TemplateView):
    template_name =  'payment_detailsview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = payment_detailstable.objects.all()
        context = {"user_data": user_data}
        return context
    
def coursevideo(request):
    return render(request,"course/course-video.html",context=None)

