from django.contrib import admin
from . models import *

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
admin.site.register(Department,DepartmentAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display=['name','slug','department','available']
    list_editable=['department','available']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Doctor,DoctorAdmin)
