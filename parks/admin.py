from django.contrib import admin
from .models import Park, Trail

class ParkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class TrailAdmin(admin.ModelAdmin):
    list_display = ("name", "park_id")

admin.site.register(Park, ParkAdmin)
admin.site.register(Trail, TrailAdmin)