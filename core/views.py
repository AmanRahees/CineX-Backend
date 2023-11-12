from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import CustomUser
from core.serializers import *

# Create your views here.

class AdminLoginAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_superadmin == True:
                refresh = RefreshToken.for_user(user)
                refresh['username'] = user.username
                refresh['role'] = user.role
                return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_200_OK)
            else:
                return Response({"Error": "Access Denied!"}, status=status.HTTP_403_FORBIDDEN)
        return Response({"Error": "Invalid Username or Password!"}, status=status.HTTP_401_UNAUTHORIZED)

class CustomersAPI(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        users = CustomUser.objects.exclude(is_superadmin=True)
        serializer = CustomerSerializers(users, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request):
        userId = request.data.get("userId")
        user = CustomUser.objects.get(id=userId)
        user.is_active = not user.is_active
        user.save()
        return Response(status=status.HTTP_202_ACCEPTED)
    
class MoviesAPI(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, pk=None):
        if pk is None:
            movies = Movie.objects.all()
            serializer = MovieSerializers(movies, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            try:
                movie = Movie.objects.get(pk=pk)
                serializer = MovieSerializers(movie, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        serializer = MovieSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            data = request.data.copy()
            movie = Movie.objects.get(pk=pk)
            if type(data['poster']):
                data['poster'] = movie.poster
                print(type(data['poster']))
            serializer = MovieSerializers(movie, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class BannersAPI(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, pk=None):
        if pk is None:
            banners = Banners.objects.all()
            serializer = BannerSerializers(banners, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            try:
                banner = Banners.objects.get(pk=pk)
                serializer = BannerSerializers(instance=banner, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
    def post(self, request):
        data = request.data
        id = int(data['movie'])
        banner = data['banner']
        try:
            movie = Movie.objects.get(id=id)
            instance = Banners.objects.create(
                movie = movie,
                banner = banner
            )
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            banner = Banners.objects.get(pk=pk)
            banner.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
