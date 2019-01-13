from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('trips/', views.browser, name='browser'),
    path('trips/create/', views.trip_create, name='trip_create'),
    path('trips/<int:trip_id>/', views.trip_detail, name='trip_detail'),
    path('trips/<int:pk>/edit/', views.trip_edit, name='trip_edit'),
    path('trips/<int:pk>/delete/', views.trip_delete, name='trip_delete'),
]