from rest_framework import serializers
from movies.models import Movie, Banners

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

class BannerSerialzier(serializers.ModelSerializer):
    movie = MovieSerializer()
    class Meta:
        model = Banners
        fields = "__all__"