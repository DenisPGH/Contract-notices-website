from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model

from ContractWebsite.first.models import Notice

User=get_user_model()
@admin.register(Notice)
class TaskNotice(admin.ModelAdmin):
    list_display = ('date','notice_number','tender_name')

