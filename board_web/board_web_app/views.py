from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm
from .models import Trip

def index(request):
    latest_trips_list = Trip.objects.order_by('-pub_date')[:5]
    context = {
        'latest_trips_list': latest_trips_list,
    }
    return render(request, 'board_web_app/index.html', context)

def trip_detail(request, trip_id):
	trip = get_object_or_404(Trip, pk=trip_id)
	return render(request, 'board_web_app/trip_detail.html', {'trip': trip})

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'