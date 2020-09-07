from django.contrib import admin
from .models import Plan,Enquiry, Equipment, Member

# Register your models here.

admin.site.register(Plan)
admin.site.register(Enquiry)
admin.site.register(Equipment)
admin.site.register(Member)