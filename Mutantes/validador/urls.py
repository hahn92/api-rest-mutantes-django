# Django
from django.urls import path

# Views
from validador import views

urlpatterns = [

    path(
        route='',
        view=views.Validador,
        name='GetValidador'
    ),

]