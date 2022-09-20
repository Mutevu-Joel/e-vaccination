from django.contrib import admin
from .models import vaccine

from .models import Child
from .models import Profile


from .models import Staff

from django.contrib.auth.models import Group

class VaccineAdmin(admin.ModelAdmin):
    list_display = ('vaccine_id','mode_of_admission','vaccine_type','vaccine_quantity')
    list_filter = ['vaccine_type','mode_of_admission']

class ChildAdmin(admin.ModelAdmin):
    list_display = ('child_registration_no', 'Surname', 'Other_name', 'weight','height','DOB','parent_ID','phone_no','ward','Underlying_condition','immunization_type','immunization_dose_no','immunization_description')


admin.site.site_header = 'KIBWEZI SUBCOUNTY HOSPITAL'
# Register your models here.
admin.site.register(vaccine,VaccineAdmin)
admin.site.unregister(Group)
admin.site.register(Staff)
admin.site.register(Profile)

admin.site.register(Child,ChildAdmin)
