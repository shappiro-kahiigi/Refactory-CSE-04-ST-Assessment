from django import forms
from .models import PassengerInformation

class PassengerInformationForm(forms.Form):
    class Meta:
        model = PassengerInformation
        fields = ['fullname', 'age', 'gender', 'departure_airport', 'arrival_airport', 'departure_date', 'departure_time', 'return_date', 'return_time']
        
        

class passportInformationForm(forms.Form):
            passport_number = forms.CharField(label='Passport Number', max_length=100)
            class Meta:
                model = PassengerInformation
        