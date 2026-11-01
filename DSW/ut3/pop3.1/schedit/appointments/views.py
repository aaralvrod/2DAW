from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import AddAppointmentForm
from .models import Appointment


@login_required
def appointment_list(request):
    appointment = Appointment.objects.all()
    return render(request, 'appointments/appointment/list.html', {'appointment': appointment})


@login_required
def appointment_detail(request, appointment_pk):
    appointment = Appointment.objects.get(pk=appointment_pk)
    return render(request, 'appointments/appointment/detail.html', {'appointment': appointment})


@login_required
def add_appointment(request):
    if request.method == 'POST':
        if (form := AddAppointmentForm(request.POST)).is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('appointments:appointment-detail', appointment_pk=appointment.pk)
    else:
        form = AddAppointmentForm()
    return render(request, 'appointments/appointment/add.html', dict(form=form))
