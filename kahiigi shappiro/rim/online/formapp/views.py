from django.shortcuts import render, redirect
from .models import PassengerInformation
from .forms import PassengerInformationForm

def home(request):
    return render(request, '/formapp/home.html')

def passenger_information(request):
    passenger_information = PassengerInformation.objects.all()
    return render(request, 'passenger_information.html', {'passenger_information': passenger_information})

def add_passenger_information(request):
    if request.method == 'POST':
        form = PassengerInformationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('passenger_information')
    else:
        form = PassengerInformationForm()
    
    return render(request, 'add_passenger_information.html', {'form': form})
