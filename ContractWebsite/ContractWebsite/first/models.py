from django.db import models

# Create your models here.

class Notice(models.Model):
    NOTICE_NUMBER_MAX_LENGHT=10
    TENDER_NAME_NUMBER_MAX_LENGHT=150
    STATE_MAX_LENGHT=30
    CONTRACT_TYPE_MAX_LENGHT=40
    TYPE_PROCUREMENT_MAX_LENGHT=40


    date=models.DateTimeField()
    notice_number=models.CharField(
        max_length=NOTICE_NUMBER_MAX_LENGHT
    )
    tender_name=models.CharField(
        unique=True,
        max_length=TENDER_NAME_NUMBER_MAX_LENGHT,
    )
    procedure_state=models.CharField(
        max_length=STATE_MAX_LENGHT

    )
    contract_type=models.CharField(
        max_length=CONTRACT_TYPE_MAX_LENGHT

    )
    type_of_procurement=models.CharField(
        max_length=TYPE_PROCUREMENT_MAX_LENGHT

    )
    estimated_value=models.FloatField()


