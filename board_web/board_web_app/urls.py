from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', views.index, name='index'),
    path('<int:trip_id>/', views.trip_detail, name='trip_detail'),
]