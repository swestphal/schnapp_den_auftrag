from django.contrib import admin
from .models import Job, Application


# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Job, JobAdmin)
admin.site.register(Application)