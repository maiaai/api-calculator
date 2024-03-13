from django.urls import path

from calc_api_v2 import views

urlpatterns = [
    path('calculate/', views.CalculatorAPIView.as_view(), name='calculate'),
]
