from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render,resolve_url
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ReservationForm
from .models import Reservation


class ReservationFormView(LoginRequiredMixin, generic.FormView):
    template_name = 'reservation/reservation_form.html'
    form_class = ReservationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
