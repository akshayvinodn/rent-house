
from django.urls import path
from rent import views
urlpatterns = [
    path('',views.index,name='index'),
    path('rents',views.rent,name='rent'),
    path('form',views.form,name='form'),
]