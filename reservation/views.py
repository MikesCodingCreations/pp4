from .models import Reservation
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ReserveTableForm

def reserve_table(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()
            return redirect('reservation:thank_you')

    context = {'form': reserve_form}
    return render(request, 'reservation/reservation.html', context)

def thank_you(request):
    return render(request ,'reservation/thank_you.html')

