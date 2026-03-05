from django.urls import path
from rango import views

app_name = 'rango'
# Map empty string to the index view
urlpatterns = [
    path('', views.index, name='index'),
]