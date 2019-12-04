from django.urls import include, path

from .views import (
    get_countries, add_country
)

urlpatterns = [
    path('countries/', get_countries, name="secure.countries"),
    path('countries/add/', add_country, name="secure.country.add"),
    path('countries/<int:pk>/', detail_country, name="secure.country.detail"),

]
