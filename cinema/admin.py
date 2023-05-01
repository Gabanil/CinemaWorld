from django.contrib import admin
from .models import Category, Actor, Genre, Movie, MovieShots, Session, Reservation, Hall, Hall_type
# Register your models here.


admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Genre)


admin.site.register(Movie)

admin.site.register(MovieShots)

admin.site.register(Session)
admin.site.register(Reservation)
admin.site.register(Hall)
admin.site.register(Hall_type)