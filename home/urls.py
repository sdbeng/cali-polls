from django.urls import path
from . import views

urlpatterns = [
    # home view
    path('', views.index)
]