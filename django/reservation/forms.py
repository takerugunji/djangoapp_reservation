import bootstrap_datepicker_plus as datetimepicker
from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ('check_in', 'check_out', 'zip_code', 'address1', 'address2',) # 'last_name', 'first_name', 'email', 'phone', 
        widgets = {
            'check_in': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ).start_of('期間'),

            'check_out': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ).end_of('期間'),

            'zip_code': forms.TextInput(attrs={'onKeyUp': "AjaxZip3.zip2addr('zip_code', '', 'address1', 'address2',)"}),
        }
