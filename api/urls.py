# from django.contrib import admin
from django.urls import path, include
from .views import RoomView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('room', RoomView.as_view())
]