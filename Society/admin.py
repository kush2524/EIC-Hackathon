
# admin.py

from django.contrib import admin
from .models import Society,ResidentProblem
class SocietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'secretary_uid', 'resident_uid')

admin.site.register(Society, SocietyAdmin)
admin.site.register(ResidentProblem)


# Register your models here.
