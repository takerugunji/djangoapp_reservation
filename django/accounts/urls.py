from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('profile_edit/<int:pk>/', views.ProfileEditView.as_view(), name='profile_edit'),
    path('delete_confirm', TemplateView.as_view(
        template_name='delete_confirm.html'), name='delete-confirmation'),
    path('delete_complete', views.DeleteView.as_view(), name='delete-complete'),
]
