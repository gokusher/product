from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('current_date/', views.current_date, name='current_date'),
    path('goodby/', views.goodby, name='goodby'),
]