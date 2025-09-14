from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_date', 'profile_photo ')}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_date', 'profile_photo ')}),)
    list_display = ['username', 'email', 'date_of_date', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
    