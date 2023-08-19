from django.contrib import admin
from .models import *
# Register your models here.

class NamesAdmin(admin.ModelAdmin):
    list_display = ['name','mobile_number','father_name','dob']
    list_filter = ['dob']
    search_fields = ['name']


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['name','day','is_present']
    list_filter = ['is_present']
    search_fields = ['name']

admin.site.register(Names,NamesAdmin)
admin.site.register(Attendance,AttendanceAdmin)