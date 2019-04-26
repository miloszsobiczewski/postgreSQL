from django.db import models


class Movie(models.Model):
    movie_id = models.CharField(unique=True, max_length=9, primary_key=True)
    title_type = models.CharField(max_length=100)
    primary_title = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200)
    is_adult = models.IntegerField()
    start_year = models.IntegerField(blank=True, null=True)
    end_year = models.IntegerField(blank=True, null=True)
    runtime_minutes = models.IntegerField(blank=True, null=True)
    genres = models.CharField(max_length=200)

    def __str__(self):
        return self.primary_title


class Actor(models.Model):
    actor_id = models.CharField(unique=True, max_length=9, primary_key=True)
    primary_name = models.CharField(max_length=100)
    birth_year = models.IntegerField(null=True)
    death_year = models.IntegerField(blank=True, null=True)
    primary_profession = models.CharField(max_length=100)
    known_for_titles = models.CharField(max_length=100)

    def __str__(self):
        return str(self.primary_name)


class MovieActorAssoc(models.Model):
    class Meta:
        unique_together = (('actor_id', 'movie_id'),)

    actor_id = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.actor_id) + '/' + str(self.movie_id)






