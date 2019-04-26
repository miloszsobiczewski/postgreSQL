from rest_framework import serializers
from .models import Movie, Actor


class MovieSerializer(serializers.ModelSerializer):
    # omdb_details = serializers.CharField(read_only=True)

    class Meta:
        model = Movie
        fields = ('movie_id', 'title_type', 'primary_title', 'original_title', 'is_adult', 'start_year', 'end_year', 'runtime_minutes', 'genres')
