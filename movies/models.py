from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=50, null=False)
    poster = models.ImageField(upload_to="posters/")
    overview = models.TextField(default="Nil")
    genre = models.CharField(max_length=256)
    language = models.CharField(max_length=50)
    runtime = models.CharField(max_length=50)
    ratings = models.FloatField(null=True)
    director = models.CharField(max_length=100, null=True)
    casts = models.TextField(null=True)
    status = models.CharField(max_length=100, default="Upcoming")
    release_date = models.DateField()

    def __str__(self):
        return self.title

class Banners(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    banner = models.ImageField(upload_to="banners/")

    def __str__(self):
        return f"{self.movie} --> {self.banner}"