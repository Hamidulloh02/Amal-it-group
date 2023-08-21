from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView
from .serializers import NewsSerializer
from .models import News
# Create your views here.

class NewsView(CreateAPIView,ListAPIView,RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsSingle(RetrieveUpdateDestroyAPIView,CreateAPIView,ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
