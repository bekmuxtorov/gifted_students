from django.contrib.auth.forms import UserCreationForm as OldUserCreationForm, UserChangeForm as OldUserChangeForm

from .models import CustomUser


class UserCreationForm(OldUserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "first_name")


class UserChangeForm(OldUserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name",
                  "status", "is_staff", "is_superuser")
