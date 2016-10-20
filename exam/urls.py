"""exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from apps.login.models import User

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^exam1/', include('apps.exam1.urls', namespace='exam')),
    url(r'^', include('apps.login.urls', namespace='login')),
]
