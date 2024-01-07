from django.contrib import admin
from service.models import service
class ServiceAdmin(admin.ModelAdmin):
    list_display=('name','lastname','email')
admin.site.register(service)

# Register your models here.
