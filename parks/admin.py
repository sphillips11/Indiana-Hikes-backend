from django.contrib import admin
from .models import Park

class ParkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Park, ParkAdmin)