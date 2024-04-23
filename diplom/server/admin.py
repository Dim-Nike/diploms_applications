from django.contrib import admin
from .models import *

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'link']

class ScientificSupervisorAdmin(admin.ModelAdmin):
    list_display = ['name']

class PaymentUserAdmin(admin.ModelAdmin):
    list_display = ['data_start', 'paid']

class LastFileAdmin(admin.ModelAdmin):
    list_display = ['data_start']


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'topic', 'price', 'is_design', 'is_design']
    list_filter = ['scientific_supervisor', 'is_technical_part', 'is_design']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(DevFile)
admin.site.register(ScientificSupervisor, ScientificSupervisorAdmin)
admin.site.register(PaymentUser, PaymentUserAdmin)
admin.site.register(LastFile, LastFileAdmin)
admin.site.register(Application, ApplicationAdmin)
