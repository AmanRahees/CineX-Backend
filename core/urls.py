from django.urls import path
from core.views import *

urlpatterns = [
    path("login", AdminLoginAPI.as_view(), name="adminLoginAPI"),

    # Customer
    path("customers", CustomersAPI.as_view(), name="customers"),

    # Movies
    path("movies", MoviesAPI.as_view(), name="movies"),
    path("movie/<int:pk>", MoviesAPI.as_view(), name="movie"),

    path("banners", BannersAPI.as_view(), name="banners"),
    path("banner/<int:pk>", BannersAPI.as_view(), name="banner"),
]