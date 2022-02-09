from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('process-data/', views.process, name='process-data'),
]