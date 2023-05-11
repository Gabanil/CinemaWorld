from django.db import models
from datetime import date
from datetime import timedelta

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
    duration = models.IntegerField("Тривалість", default=0)

    category = models.ForeignKey(
        Category, verbose_name="Категорія", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return f"{self.title}, {self.duration} min"
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


class Hall_type(models.Model):
    type = models.CharField("Тип залу", max_length=20)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Тип залу"
        verbose_name_plural = "Тип залів"


class Hall(models.Model):
    number = models.IntegerField("Номер залу", unique=True)
    stage = models.IntegerField("Етаж")
    places = models.IntegerField("Кіл-ть місць")

    type = models.ForeignKey(
        Hall_type, verbose_name="Тип залу", on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return "Зал " + str(self.number)

    class Meta:
        verbose_name = "Зал"
        verbose_name_plural = "Зали"


class Reservation(models.Model):
    client_name = models.CharField("Імʼя клієнта", max_length=100)
    place_num = models.IntegerField("Місце")
    paid = models.BooleanField("Оплачено")
    date_resevation = models.DateTimeField("Дата та час")

    def __str__(self):
        return self.client_name, self.place_num

    class Meta:
        verbose_name = "Резервація"
        verbose_name_plural = "Резервації"


class Session(models.Model):
    hall_id = models.ForeignKey(Hall, verbose_name="Зал", on_delete=models.SET_NULL, null=True)
    movie_id = models.ForeignKey(Movie, verbose_name="Фільм", on_delete=models.SET_NULL, null=True)
    start = models.DateTimeField("Початок")
    end = models.DateTimeField("Кінець", blank=True, null=True)
    # default = start + timedelta(minutes=movie_id.duration)

    class Meta:
        verbose_name = "Сеанс"
        verbose_name_plural = "Сеанси"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        duration = self.movie_id.duration
        self.end = self.start + timedelta(minutes=duration)
        self.__class__.objects.filter(pk=self.pk).update(end=self.end)

    def __str__(self):
        return f"Сеанс {self.movie_id}, start at {self.start}, in {self.hall_id}"