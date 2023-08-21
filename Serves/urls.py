from django.urls import path

from .views import ServesView,ServesSingle

urlpatterns  = [
    path('',ServesView.as_view()),
    path('<int:pk>/',ServesSingle.as_view())
]