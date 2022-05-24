from django.contrib import admin
from .models import Perfume
# Register your models here.

@admin.register(Perfume)
class AdminPerfume(admin.ModelAdmin):
    list_display = ['perfume_name', 'purchaser', 'date_updated']