from django.contrib import admin
from .models import *

# Register your models here.

class TrackingAdmin(admin.ModelAdmin):
    list_display = ('name','tracking','tel')

admin.site.register(Tracking,TrackingAdmin)
admin.site.register(Runner)
admin.site.register(Ask)
