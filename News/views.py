from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView
from .serializers import NewsSerializer
from .models import News
# Create your views here.

class NewsView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
