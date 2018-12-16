from django.contrib import admin
from .models import GuestEmail, User

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm


# THIS IS MY PREVIOUS ONE
# ------------------------
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['email', 'get_full_name', 'is_active', 'timestamp']
#     search_fields = ['email', 'first_name', 'last_name']
#     fields = ['email', 'password', ('first_name', 'last_name'), ('active', 'staff', 'admin'), 'last_login']
#
#     form = UserAdminChangeForm  # EDIT VIEW/UPDATE View
#     add_form = UserAdminCreationForm # Create View


# THIS MIC CURRENT ONE
# -----------------------
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'get_full_name', 'admin', 'active', 'timestamp')
    list_filter = ('admin', 'staff', 'active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': (('first_name', 'last_name'), 'last_login')}),
        ('Permissions', {'fields': ('admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'email', 'password1', 'password2')}
         ),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(GuestEmail)
admin.site.register(User, UserAdmin)
