"""theater_lab URL Configuration

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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (DirectorViewSet, TheaterViewSet, HallViewSet, ActorViewSet,
                    PlayViewSet, RoleViewSet, BuyerViewSet, SeatViewSet,
                    ScheduleViewSet, TicketViewSet)

router = DefaultRouter()
router.register(r'directors', DirectorViewSet, basename='director')
router.register(r'theaters', TheaterViewSet, basename='theater')
router.register(r'halls', HallViewSet, basename='hall')
router.register(r'actors', ActorViewSet, basename='actor')
router.register(r'plays', PlayViewSet, basename='play')
router.register(r'roles', RoleViewSet, basename='role')
router.register(r'buyers', BuyerViewSet, basename='buyer')
router.register(r'seats', SeatViewSet, basename='seat')
router.register(r'schedules', ScheduleViewSet, basename='schedule')
router.register(r'tickets', TicketViewSet, basename='ticket')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
path('theater/', include('actors.urls')),

]
