from django.urls import path

from . import views

app_name = 'reservation'

urlpatterns = [
    path('reservation_form/', views.ReservationFormView.as_view(), name='reservation_form'),
    path('reservation_confirm/', views.ReservationFormView.as_view(), name='reservation_confirm'),
]