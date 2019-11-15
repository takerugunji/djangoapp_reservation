"""myblogapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from posts import views
from django.views.generic import RedirectView
from .views import ContactFormView, ContactResultView

urlpatterns = [
    path('',RedirectView.as_view(url='posts/')), 
    path('posts/', include('posts.urls')),
    path('posts/<post_id>/', views.post_detail, name="post_detail"),
    path('accounts/', include('accounts.urls')),
    path('reservation/', include('reservation.urls')),
    path('posts/', include('django.contrib.auth.urls')), # 1. 元々提供されている機能へ振り分け
    path('accounts/', include('django.contrib.auth.urls')), # 振り分け posts? accounts?
    path('admin/', admin.site.urls),
    path('auth/', include('allauth.urls')),
    path('contacts/', ContactFormView.as_view(), name='contact_form'),
    path('contacts/result/', ContactResultView.as_view(), name='contact_result'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)