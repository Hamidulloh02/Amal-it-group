from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView
from Serves.models import Serves
from .serializers import ServesSerializers


class ServesView(ListAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView):
    queryset = Serves.objects.all()
    serializer_class = ServesSerializers

class ServesSingle(RetrieveUpdateDestroyAPIView,CreateAPIView,ListAPIView):
    queryset = Serves.objects.all()
    serializer_class = ServesSerializers

    