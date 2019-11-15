from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render,resolve_url
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import (
     get_user_model, logout as auth_logout,
)
from .forms import UserCreateForm, ProfileEditForm
# from django.test import Client, TestCase

User = get_user_model()

# class UserloginTestCase(TestCase):
    # def setUp(self):
        # self.user = User.objects.create_user('TestUser', 'test@test.com', '2222test')
        # self.client = Client()
        # self.client.login(username='test@test.com', password='2222test')
        # self.csrf_client = Client(enforce_csrf_checks=True)

class SignUpView(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ProfileView(LoginRequiredMixin, generic.View):

    def get(self, *args, **kwargs):
        return render(self.request,'profile.html')


class DeleteView(LoginRequiredMixin, generic.View):

    def get(self, *args, **kwargs):
        user = User.objects.get(email=self.request.user.email)
        user.is_active = False
        user.save()
        auth_logout(self.request)
        return render(self.request,'delete_complete.html')

class ProfileEditView(LoginRequiredMixin,generic.UpdateView):
    model = User
    form_class = ProfileEditForm
    template_name = 'profile_edit.html'

    def get_success_url(self):
        return resolve_url('accounts:profile', pk=self.kwargs['pk'])