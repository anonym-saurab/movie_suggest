from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    mood = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    release_date = models.DateField()
    imdb_rating = models.FloatField()

    def __str__(self):
        return self.title
    

