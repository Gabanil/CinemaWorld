from django.db import models
from datetime import date

from django.urls import reverse


class Category(models.Model):
    """Категорії"""
    name = models.CharField("Категорія", max_length=150)
    description = models.TextField("Опис")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class Actor(models.Model):
    """Актори та режисери"""
    name = models.CharField("Імʼя", max_length=100)
    age = models.PositiveSmallIntegerField("Вік", default=0)
    description = models.TextField("Опис")
    image = models.ImageField("Зображення", upload_to="actors/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actor_detail', kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Актори та режисери"
        verbose_name_plural = "Актори та режисери"


class Genre(models.Model):
    """Жанри"""
    name = models.CharField("Імʼя", max_length=100)
    description = models.TextField("Опис")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанри"


class Movie(models.Model):
    """Фільм"""
    title = models.CharField("Назва", max_length=100)
    # tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Опис")
    poster = models.ImageField("Постер", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Дата виходу", default=2019)
    country = models.CharField("Країна", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="Режисер", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="Актори", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="Жанри")
    world_premiere = models.DateField("Премʼєра в світі", default=date.today)

    category = models.ForeignKey(
        Category, verbose_name="Категорія", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    # def get_review(self):
    #     return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Фільм"
        verbose_name_plural = "Фільми"


class MovieShots(models.Model):
    """Кадри з фільму"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Опис")
    image = models.ImageField("Зображення", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Фільм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр з фільму"
        verbose_name_plural = "Кадри з фільму"



# class Reviews(models.Model):
#     """Отзывы"""
#     email = models.EmailField()
#     name = models.CharField("Имя", max_length=100)
#     text = models.TextField("Сообщение", max_length=5000)
#     parent = models.ForeignKey(
#         'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
#     )
#     movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.name} - {self.movie}"
#
#     class Meta:
#         verbose_name = "Отзыв"
#         verbose_name_plural = "Отзывы"
