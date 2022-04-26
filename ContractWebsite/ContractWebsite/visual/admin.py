from django.contrib import admin

# Register your models here.
from ContractWebsite.first.models import Notice


@admin.register(Notice)
class TaskNotice(admin.ModelAdmin):
    list_display = ('date','notice_number','tender_name')
