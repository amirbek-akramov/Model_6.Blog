from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser


@admin.action(description="Block selected user")
def block_user(modeladmin, request, queryset):
    queryset.update(block=True)


@admin.action(description="Unblock selected user")
def unblock_user(modeladmin, request, queryset):
    queryset.update(block=False)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    actions = [block_user, unblock_user]

    list_display = ('email', 'username', 'first_name', 'last_name', 'birth_date', 'is_active', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('birth_date', 'country', 'block')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('birth_date', 'country', 'block')}),
    )
