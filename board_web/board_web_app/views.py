from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic
from django.utils import timezone
from .forms import CustomUserCreationForm, TripForm
from .models import Trip


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def browser(request):
    latest_trips_list = Trip.objects.order_by('-pub_date')[:5]
    context = {
        'latest_trips_list': latest_trips_list,
    }
    return render(request, 'board_web_app/browser.html', context)

def trip_detail(request, trip_id):
	trip = get_object_or_404(Trip, pk=trip_id)
	return render(request, 'board_web_app/trip_detail.html', {'trip': trip})

def trip_create(request):
    if request.method == "POST":
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.organiser = request.user
            trip.pub_date = timezone.now()
            trip.save()
            return render(request, 'board_web_app/trip_detail.html', {'trip': trip})
    else:
        form = TripForm()
    return render(request, 'board_web_app/trip_editor.html', {'form': form})

def trip_edit(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == "POST":
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.organiser = request.user
            trip.pub_date = timezone.now()
            trip.save()
            return render(request, 'board_web_app/trip_detail.html', {'trip': trip})
    else:
        form = TripForm(instance=trip)
    return render(request, 'board_web_app/trip_editor.html', {'form': form})


def trip_delete(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    trip.delete()
    return redirect('browser')

