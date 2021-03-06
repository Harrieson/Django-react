# from django.contrib import admin
from django.urls import path
from .views import JoinRoom, LeaveRoom, RoomView, CreateRoomView, GetRoom, UserInRoom

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('room', RoomView.as_view()),
    path('create-room', CreateRoomView.as_view()),
    path('get-room', GetRoom.as_view()),
    path('join-room', JoinRoom.as_view()),
    path('user-in-room', UserInRoom.as_view()),
    path('leave-room', LeaveRoom.as_view())

]
