from django.contrib import admin
from accounts.models import CustomUser
from movies.models import Movie, Banners

admin.site.register(CustomUser)
admin.site.register(Movie)
admin.site.register(Banners)