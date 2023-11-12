from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from movies.serializers import MovieSerializer, BannerSerialzier
from movies.models import Movie, Banners

class HomeAPI(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        movies = Movie.objects.all()
        movie_serializer = MovieSerializer(movies, many=True)
        banners = Banners.objects.all()
        banner_serializer = BannerSerialzier(banners, many=True)
        context = {
            "movies": movie_serializer.data,
            "banners": banner_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)