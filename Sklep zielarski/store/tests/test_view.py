from importlib import import_module
from unittest import skip

from django.conf import settings
from django.http import HttpRequest
from django.test import Client, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import product_all

User = settings.AUTH_USER_MODEL


@skip('test skipping')
class TestSkip(TestCase):
    def test_skip_exmaple(self):
        pass


class TestViewResponse(TestCase):

    def setUp(self):
        self.c = Client()
        User.obejcts.create(username='admin')
        Category.objects.create(name='olej', slug='olej')
        Product.objects.create(category_id=5, title='miod', created_by_id=5,
                               slug='miod', price='20.00', image='sss')

    def test_homepage_url(self):
        """
        Test homepage response status
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/', HTTP_HOST='addres.pl')
        self.assertEqual(response.status_code, 400)
        response = self.c.get('/', HTTP_HOST='domena.pl')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test product detail URL
        """
        response = self.c.get(reverse('store:product_detail', args=['miod']))
        self.assertEqual(response.status_code, 200)

    def test_product_list_url(self):
        """
        Test product list url
        """
        response = self.c.get(reverse('store:category_list', args=['olej']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """
        Code validation, search HTML for text
        """
        request = HttpRequest()
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()
        response = product_all(request)
        html = response.content.decode('utf8')
        self.assertIn('<title> Zielarz </title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

