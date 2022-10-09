"""chatterbox_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

import base.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', base.views.hello),
    path('search/', base.views.search, name='search'),
    path('room/<pk>', base.views.room, name='room'),
    path('', base.views.RoomsView.as_view(), name='rooms'),
    path('room_create/', base.views.RoomCreateView.as_view(), name='room_create'),
]
