from django.contrib import admin
from .models import Park, Trail

class ParkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Park, ParkAdmin)
admin.site.register(Trail)