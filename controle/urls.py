from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('controle/<int:id>', views.controleview, name = 'controleview'),      

]