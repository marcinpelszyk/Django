import os
import sys

import pytest
from rest_framework.test import APIClient

# from showtimes.models import Cinema, Screening
from .utils import faker, create_fake_cinema, create_fake_screening

sys.path.append(os.path.dirname(__file__))


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.fixture
def set_up():
    for _ in range(3):
        create_fake_screening()
    for _ in range(3):
        create_fake_cinema()



