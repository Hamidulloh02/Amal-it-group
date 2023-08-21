from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView
from Portfolio.models import Portfolio
from .serializers import PortfolioSerializers

# Create your views here.


class PortfolioView(ListAPIView,RetrieveUpdateAPIView,CreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializers

class PortfoliosingleView(RetrieveUpdateDestroyAPIView,CreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializers