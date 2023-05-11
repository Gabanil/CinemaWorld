from django.shortcuts import render
from rest_framework.views import APIView
from .models import Movie
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class MovieAPIView(APIView):
    def index(request):
        movies = Movie.objects.all()
        return render(request, "index.html", {"movies": movies})


class MovieDetailAPIView(APIView):
    def index(request):
        movies = Movie.objects.all()
        return render(request, "description.html")


class ResevationAPIView(APIView):
    def index(request):
        movies = Movie.objects.all()
        return render(request, "reservation.html")

 #    шаблон вьюшки
 # @swagger_auto_schema(
    #     operation_summary="Get a dish by slug",
    #     operation_description="<b>Retrieve a single dish by its unique slug.</b>",
    #     responses={200: Dish_Serializer()},
    #     tags=["Pages"])
    # def get(self, request, slug):
    #     try:
    #         movies = Movie.objects.all()
    #         # serializer = Dish_Serializer(dish, context={'request': request})
    #         print(movies)
    #         return Response(movies)
    #     except Movie.DoesNotExist:
    #         return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)