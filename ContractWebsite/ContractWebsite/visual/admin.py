from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model

from ContractWebsite.first.models import Notice
from ContractWebsite.visual.models import DateModel

User=get_user_model()
@admin.register(Notice)
class TaskNotice(admin.ModelAdmin):
    list_display = ('date','notice_number','tender_name')


@admin.register(DateModel)
class TaskDateModel(admin.ModelAdmin):
    list_display = ('id','start_date','end_date')

