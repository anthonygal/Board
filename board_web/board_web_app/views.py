from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import trip
# Create your views here.
from django.http import HttpResponse


def index(request):
    latest_trips_list = trip.objects.order_by('-pub_date')[:5]
    template = loader.get_template('board_web_app/index.html')
    context = {
        'latest_trips_list': latest_trips_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
	return HttpResponse("You're looking at trip %s." % trip_id)