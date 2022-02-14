from django.contrib import admin
from .models import Hiker, Hike

class HikerAdmin(admin.ModelAdmin):
    list_display = ("name", "registered")

admin.site.register(Hiker, HikerAdmin)
admin.site.register(Hike)
