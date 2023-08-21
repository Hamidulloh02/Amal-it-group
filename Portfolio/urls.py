from django.urls import path

from .views import PortfolioView,PortfoliosingleView

urlpatterns = [
    path('',PortfolioView.as_view()),
    path('<int:pk>/', PortfoliosingleView.as_view())
]