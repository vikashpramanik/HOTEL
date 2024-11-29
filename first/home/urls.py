from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path("" , views.home , name='home'),
   path("about" , views.about , name='about'),
   path("services" , views.services , name='services'),
   path("rooms" , views.rooms , name='rooms'),
   path("gallary" , views.gallary , name='gallary'),
   path("contact" , views.contact , name='contact'),
]