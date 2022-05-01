from django import forms


from ContractWebsite.visual.models import DateModel
from bootstrap_datepicker_plus.widgets import DatePickerInput


class SearchConditionForm(forms.ModelForm):
    class Meta:
        model=DateModel
        fields="__all__"
        widgets = {
            'start_date':DatePickerInput,
            'end_date':DatePickerInput,
        }



