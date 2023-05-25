from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .models import Movie, Session, Reservation
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .forms import ReservationForm


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
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            sessions = Session.objects.filter(movie_id=pk)

            reg_form = ReservationForm()

            context = {
                'movie': movie,
                'form': reg_form,
                'sessions': sessions

            }
            return render(request, "reservation.html", context)

        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        except Session.DoesNotExist:
            return Response({'error': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        form = ReservationForm(request.POST)

        if form.is_valid():
            form.save()
            return Response({'success': 'Form Saved'})
        else:
            return Response({'error': 'Form Not Correct'}, status=status.HTTP_400_BAD_REQUEST)


class SessionsViewList(APIView):

    def get(self, request):
        sessions = Session.objects.all().order_by("movie_id")
        unique_movies = sessions.values("movie_id").distinct()

        context = {
            'sessions': sessions,
            'movies': unique_movies
        }

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


def get_reservations(request):
    session_id = request.GET.get('session_id')
    reservations = Reservation.objects.filter(session_id=session_id)
    places_num = list(reservations.values("place_num"))  # get only place numbers
    place_nums = [item['place_num'] for item in places_num]  # places queryset into list

    data = {
        'place_nums': place_nums,
    }
    return JsonResponse(data)
