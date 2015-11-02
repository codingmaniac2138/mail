from django.contrib import admin
from .models import *
# Register your models here.

class edit_profile_admin(admin.ModelAdmin):
    list_display = ['user','id_field','pass_field',]

    class Meta:
        model = edit_profile

admin.site.register(edit_profile,edit_profile_admin)
