from django.urls import path
from . import views

app_name = "cardeal"
urlpatterns = [
    path("" , views.home, name= 'home'),
    path("about" , views.about, name= 'about'),
    path("services" , views.services, name= 'services'),
    path("contact" , views.contact, name= 'contact'),
    ###detail view
    path("detail/<int:id>/name" , views.detail, name= 'detail'),

]