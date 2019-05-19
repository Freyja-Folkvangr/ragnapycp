from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Login

@admin.register(Login)
class MyUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        ('Ragnarok Settings', {'fields': ('sex', 'birthdate', 'character_slots')}),
        ('Ragnarok Privileges', {'fields': ('state', 'group_id', 'vip_time', 'old_group')}),
        ('Ragnarok Security',
         {'fields': ('pincode', 'pincode_change', 'unban_time', 'expiration_time', 'logincount', 'last_ip')})
    )
    list_display = ('username', 'id', 'email', 'is_staff', 'is_active', 'state')
    search_fields = ['id', 'username', 'email']
