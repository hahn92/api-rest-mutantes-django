# Django
from django.urls import path

# Views
from validador import views

urlpatterns = [

    path(
        route='mutant/',
        view=views.Validador,
        name='GetValidador'
    ),

    path(
        route='stats/',
        view=views.Estadisticas,
        name='GetValidador'
    ),

]