from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from . forms import CustomUserChangeForm, CustomUserCreateForm

CustomUser = get_user_model()


class CustomAdmin(UserAdmin):
    add_form = CustomUserCreateForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', ]


admin.site.register(CustomUser, CustomAdmin)
