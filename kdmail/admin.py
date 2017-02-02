from django.contrib import admin
from .models import *


# Register your models here.

class edit_profile_admin(admin.ModelAdmin):
    list_display = ['user', 'consultant_name', 'technology', 'job_location', 'requested_email', ]

    class Meta:
        model = edit_profile


class user_stats_admin(admin.ModelAdmin):
    list_display = ['user', 'consultant_name', 'technology', 'job_location', 'requested_email', 'requirements_count',
                    'date_added', ]

    class Meta:
        model = user_stats


admin.site.register(edit_profile, edit_profile_admin)
admin.site.register(user_stats, user_stats_admin)
