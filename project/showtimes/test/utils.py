from random import sample, randint, choice

from django.utils import timezone
from faker import Faker

from showtimes.models import Cinema, Screening

faker = Faker("pl_PL")


# def random_movie():
#     """Return a random Person object from db."""
#     movie = Movie.objects.all()
#     return choice(movie)


def fake_cinema_data():
    """Generate a dict of cinema data

    The format is compatible with serializers (`Cinema` relations
    represented by movies).
    """
    cinema_data = {
        'name': 'Multikino',
        'city': 'Białystok',
        'capacity': 'small',
        'movies': 'killer',
    }

    return cinema_data


def create_fake_cinema():
    """Generate new fake cinema and save to database."""
    cinema_data = fake_cinema_data()
    movies = cinema_data['movies']
    del cinema_data['movies']
    new_cinema = Cinema.objects.create(**cinema_data)
    for movie in movies:
        new_cinema.movies.add(movie)

def fake_screening_data():
    """Generate a dict of screening data
    The format is compatible with serializers 'Screening'.
    """
    screening_data = {
        'movie': 'killer',
        'cinema': 'Helios',
        'date': timezone.now()
    }

    return screening_data

def create_fake_screening():
    """Generate new fake screening """
    screening_data = fake_screening_data()
    cinemas = screening_data['cinema']
    del screening_data['cinema']
    new_screening = Screening.objects.create(**screening_data)
    for cinema in cinemas:
        new_screening.movie.add(cinema)