from django.shortcuts import render
from rest_framework.views import APIView
from .models import Movie,Session , Reservation
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class MovieAPIView(APIView):
    def index(request):
        movies = Movie.objects.all()
        return render(request, "index.html", {"movies": movies})


class MovieDetailAPIView(APIView):
    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        return render(request, "description.html", {"movie": movie})
        # return Response(movie)


class ResevationAPIView(APIView):
    def get(self, request, pk, session_id):
        movie = Movie.objects.get(pk=pk)
        session = Session.objects.get(movie_id=pk, pk=session_id)
        print(session)
        reservations = Reservation.objects.filter(session_id=session_id)
        print(reservations)
        context = {
            'movie': movie,
            'places_res': reservations
        }
        return render(request, "reservation.html", context)

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