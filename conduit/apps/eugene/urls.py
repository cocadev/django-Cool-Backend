from django.urls import path

from .views import (
    get_countries, add_country, detail_country, update_country, delete_country
)

urlpatterns = [
    path('countries/', get_countries, name="secure.countries"),
    path('countries/add/', add_country, name="secure.country.add"),
    path('countries/<int:pk>/', detail_country, name="secure.country.detail"),
    path('countries/<int:pk>/update/', update_country, name="secure.country.update"),
    path('countries/<int:pk>/delete/', delete_country, name="secure.country.delete"),

]
