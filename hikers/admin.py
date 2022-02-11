from django.contrib import admin
from .models import Hiker

class HikerAdmin(admin.ModelAdmin):
    list_display = ("name", "username", "registered")

admin.site.register(Hiker, HikerAdmin)
