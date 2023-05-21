from django.shortcuts import render
from rest_framework.views import APIView
from .models import Movie, Session, Reservation
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status


class MovieAPIView(APIView):
    def index(request):
        movies = Movie.objects.all()
        return render(request, "index.html", {"movies": movies})


class MovieDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            return render(request, "description.html", {"movie": movie})
            # return Response(movie)

        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

class ResevationAPIView(APIView):
    def get(self, request, pk, session_id):
        try:
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

        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        except Session.DoesNotExist:
            return Response({'error': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)


class SessionsViewList(APIView):

    def get(self, request):
        sessions = Session.objects.all().order_by("movie_id")
        unique_movies = sessions.values("movie_id").distinct()

        context = {
            'sessions': sessions,
            'movies': unique_movies
        }

        # print(unique_movies)
        return render(request, "reservation.html")


class MovieAvalableSession(APIView):
    def get(self, request, pk):
        try:
            sessions = Session.objects.filter(movie_id=pk)

            # for session exception because not working with filter
            if len(sessions) < 1:
                sessions = Session.objects.get(movie_id=pk)

            movie = Movie.objects.get(pk=pk)

            context = {
                'movie': movie,
                'sessions': sessions
            }
            return render(request, "sessions.html", context)

        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        except Session.DoesNotExist:
            return Response({'error': 'Sessions not found'}, status=status.HTTP_404_NOT_FOUND)


class ReservationTemplate(APIView):
    def get(self, request):
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