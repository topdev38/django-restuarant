from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    fieldsets = (
        (None, {'fields': ('email', 'firstname', 'lastname', 'password', 'company')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin', 'active')}),
    )
    list_display = ('email', 'firstname', 'lastname', 'company', 'admin')
    list_filter = ('admin',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1')}),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
