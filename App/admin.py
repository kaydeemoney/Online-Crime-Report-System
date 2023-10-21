from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(wantedperson)
admin.site.register(ComplaintRegister)
admin.site.register(missingperson)
admin.site.register(crimestories)
