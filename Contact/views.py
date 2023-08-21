from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView
from .models import Contact
from .serializers import ContactSerializer

# Create your views here.

class ContactView(CreateAPIView,ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
