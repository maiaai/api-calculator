from django.urls import path, include
from rest_framework import routers

from calc_api.views import CalculatorViewSet

router = routers.DefaultRouter()
router.register(r'calc', CalculatorViewSet, 'calc')
urlpatterns = [
    path('', include(router.urls)),
]