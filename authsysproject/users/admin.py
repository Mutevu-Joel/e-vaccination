from django.contrib import admin
from .models import vaccine
from django.contrib.auth.models import Group

class VaccineAdmin(admin.ModelAdmin):
    list_display = ('vaccine_id','vaccine_name','vaccine_type','vaccine_quantity')
    list_filter = ['vaccine_type']

admin.site.site_header = 'KIBWEZI SUBCOUNTY HOSPITAL'
# Register your models here.
admin.site.register(vaccine,VaccineAdmin)
admin.site.unregister(Group)
