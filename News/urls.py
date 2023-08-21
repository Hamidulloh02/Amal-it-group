from django.urls import path 
from .views import NewsView , NewsSingle

urlpatterns = [
    path('',NewsView.as_view()),
    path('<int:pk>/',NewsSingle.as_view())
]