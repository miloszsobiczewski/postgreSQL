from rest_framework import viewsets
from .models import Movie, Actor
from .serializers import MovieSerializer


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('primary_title')
    serializer_class = MovieSerializer

    def get_queryset(self):
        """
        Enables filtering and sorting
        """
        queryset = Movie.objects.all()

        # year filter
        start_year = self.request.query_params.get('startYear', None)
        if start_year is not None:
            queryset = queryset.filter(start_year=start_year)

        # genre filter
        genre = self.request.query_params.get('genre', None)
        if genre is not None:
            queryset = queryset.filter(genres__iregex=genre)

        return queryset

