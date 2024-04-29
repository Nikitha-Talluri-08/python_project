# admin.py
from django.contrib import admin
from .models import Userregistration, VisaApplication


class VisaApplicationAdmin(admin.ModelAdmin):
    list_display = ['user', 'passport_number', 'country_of_origin', 'purpose_of_visit', 'application_date', 'status']
    list_filter = ['status']
    search_fields = ['user__username', 'passport_number', 'country_of_origin']
    actions = ['approve_application', 'reject_application']

    def approve_application(self, request, queryset):
        queryset.update(status='Approved')

    def reject_application(self, request, queryset):
        queryset.update(status='Rejected')

    approve_application.short_description = "Approve selected visa applications"
    reject_application.short_description = "Reject selected visa applications"


admin.site.register(Userregistration)
admin.site.register(VisaApplication, VisaApplicationAdmin)
