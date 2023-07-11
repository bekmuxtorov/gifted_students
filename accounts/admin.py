from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ("email", "id", "first_name", "last_name", "status")
    list_filter = ("status",)
    fieldsets = (
        (None, {"fields": ("email", 'first_name', "last_name")}),
        ("Permissions", {"fields": (
         "status", "is_staff", "is_superuser", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "first_name", "last_name", "email", 'status', "is_staff", "is_superuser", "password1", "password2", "user_permissions"
            )}
         ),
    )
    search_fields = ("email",)
    ordering = ("email",)
