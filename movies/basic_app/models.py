from django.db import models
from django.urls import reverse
from django.db import models

class Movie(models.Model):
    movie_id = models.PositiveIntegerField(default=True)
    title = models.CharField(max_length=30)
    plot = models.TextField(max_length=360)
    director = models.CharField(max_length=30)
    length = models.CharField(max_length=10)
    released_year = models.IntegerField()
    covers = models.URLField(default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("basic_app:detail", kwargs={'pk': self.pk})


class Actor(models.Model):
    name = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, related_name='actors', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Post(models.Model):
    content = models.CharField(max_length = 200)

    def __str__(self):
        return self.content