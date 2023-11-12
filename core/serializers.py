from rest_framework import serializers
from accounts.models import CustomUser
from movies.models import Movie, Banners

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

class BannerSerializers(serializers.ModelSerializer):
    movie = MovieSerializers()
    class Meta:
        model = Banners
        fields = "__all__"