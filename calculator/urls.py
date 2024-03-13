from django.contrib import admin
from django.urls import path, include

from calc_api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include('calc_api.urls')),
    path('api_v2/', include('calc_api_v2.urls')),
]
