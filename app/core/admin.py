from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext as _ #Used - _('Personal Info')

# Register your models here.
class UserAdmin(BaseUserAdmin): # Extending the base useradmin
	ordering = ['id'] # orderby ID
	list_display = ['email', 'name'] # display only the email and name but order by ID
	# This will generate the section HTML tags for the admin page
	# None means set the title to none
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		(_('Personal Info'), {'fields': ('name',)}), # If only 1 tuple value enter a  ',' - ('name',)
		(_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
		(_('Important dates'), {'fields': ('last_login',)})
	)

	add_fieldsets = (
		(None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2')}),
	)

admin.site.register(models.User, UserAdmin)
