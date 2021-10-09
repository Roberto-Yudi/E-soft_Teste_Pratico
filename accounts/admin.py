from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['first_name', 'email', 'idade', 'nascimento',]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('idade', 'nascimento', 'observação')}),)
    add_fieldsets = UserAdmin.add_fieldsets + ( (None, {'fields': ('idade', 'nascimento','observação')}),)


admin.site.register(CustomUser, CustomUserAdmin)