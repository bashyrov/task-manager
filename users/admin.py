from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee, Position


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "position", "is_staff")
    list_filter = ("position", "is_staff", "is_superuser")
    search_fields = ("username", "email", "first_name", "last_name")

    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("position",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("position",)}),
    )