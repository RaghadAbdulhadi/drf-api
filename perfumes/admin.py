from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, PurchaseItem

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    mode = CustomUser
    list_display = ['email', 'username', 'item_number']

    fieldsets =  UserAdmin.fieldsets + (
        ("contact number", {"fields": ("item_number",)}),
    )

@admin.register(PurchaseItem)
class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ['item_price', 'item_review', 'type' ]
