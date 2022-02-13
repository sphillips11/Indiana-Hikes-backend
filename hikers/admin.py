from django.contrib import admin
from .models import Hiker, Hike

class HikerAdmin(admin.ModelAdmin):
    list_display = ("name", "username", "registered")

admin.site.register(Hiker, HikerAdmin)
admin.site.register(Hike)
