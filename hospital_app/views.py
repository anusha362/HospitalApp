from django.shortcuts import render,get_object_or_404
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage


def home(request,c_slug=None):
    c_page=None
    doc=None
    if c_slug!=None:
        c_page=get_object_or_404(Department,slug=c_slug)
        doc=Doctor.objects.filter(department=c_page,available=True)
    else:

        doc=Doctor.objects.all().filter(available=True)
    dep=Department.objects.all()
    paginator=Paginator(doc,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)
    return render(request,'index.html',{'pr':doc,'ct':dep,'pg':pro})


def doc_Details(request,c_slug,doctor_slug):
    try:
        doct=Doctor.objects.get(department__slug=c_slug,slug=doctor_slug)
    except Exception as e:
        raise e
    return render(request,'item.html',{'pr':doct})

def appointment(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        date=request.POST['date']
        time=request.POST['time']
        appointmentfor=request.POST['appointmentfor']
    

        return render(request,'appointment.html',{'name':name,
        'email':email,
        'date':date,
        'time':time,
        'appointmentfor':appointmentfor})

    else:
        return render(request,'index.html',{})

