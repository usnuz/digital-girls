from django.urls import path
from .views import *


urlpatterns = [
    path('slider/', slider),
    path('about/', about),
    path('direction/', direction),
    path('task/', task),
    path('result/', results),
    path('result/<int:pk>', result_items),
]
