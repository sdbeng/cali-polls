from django.urls import path
from . import views

app_name = 'flights'

urlpatterns = [
    # /flights/
    path('', views.index, name='index'),
]