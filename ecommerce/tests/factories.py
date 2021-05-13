import factory

from faker import Faker
fake = Faker()

from ecommerce.apps.catalogue.models import Category


####
# Catalogue
####

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "Oleje"
    slug = "oleje"

