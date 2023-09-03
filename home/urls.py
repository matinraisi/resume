from django.urls import path
from .views import homeview , GetData

urlpatterns = [
    path('',homeview),
    path('data/',GetData)

]