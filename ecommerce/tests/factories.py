import factory

from faker import Faker
fake = Faker()

from ecommerce.apps.account.models import Customer, Address
from ecommerce.apps.catalogue.models import (
    Category,
    ProductType, 
    ProductSpecification,
    ProductSpecificationValue,
    Product,
      )


####
# Catalogue
####

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "Oleje"
    slug = "oleje"

class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductType

    name = 'miody'



class ProductSpecificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductSpecification

    product_type = factory.SubFactory(ProductTypeFactory)
    name = "pages"

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    product_type = factory.SubFactory(ProductTypeFactory)
    category = factory.SubFactory(CategoryFactory)
    title = 'product_title'
    description = fake.text()
    slug = 'product_slug'
    reqular_price = '9.99'
    discount_price = '4.99'
    tax_rate = 1

class ProductSpecificationValueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductSpecificationValue

    product = factory.SubFactory(ProductFactory)
    specification = factory.SubFactory(ProductSpecificationFactory)
    value = 'oleje z dupy'


####
# Account
####


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    email = "a@a.com"
    name = "user1"
    mobile = "666777333"
    password = "tester"
    is_active = True
    is_staff = False

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        if "is_superuser" in kwargs:
            return manager.create_superuser(*args, **kwargs)
        else:
            return manager.create_user(*args, **kwargs)


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address

    customer = factory.SubFactory(CustomerFactory)
    full_name = fake.name()
    phone = fake.phone_number()
    postcode = fake.postcode()
    address_line = fake.street_address()
    address_line2 = fake.street_address()
    town_city = fake.city_suffix()