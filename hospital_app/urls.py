from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="hm"),
    path('<slug:c_slug>/',views.home,name='doc_dept'),
    path('<slug:c_slug>/<slug:doctor_slug>',views.doc_Details,name='details'),
    path('appointment.html',views.appointment,name="appointment"),

]