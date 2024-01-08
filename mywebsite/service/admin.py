from django.contrib import admin
from service.models import service
class ServiceAdmin(admin.ModelAdmin):
    list_display=('name','lastname','email','sub1','sub2','sub3','sub4','sub5')
   

admin.site.register(service,ServiceAdmin)


# Register your models here.
