from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # /products/
    path('', views.index, name='index'),
]