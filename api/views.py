from django.shortcuts import render
from rest_framework import generics
from .serializers import  RoomSerializer
from .models import Room
# from django.http import HttpResponse

# Create your views here.

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


# def main(request):
#     return HttpResponse('Hello There')
