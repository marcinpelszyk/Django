from django.test import TestCase
from django.urls import reverse
from shop.models import Category, Product
from django.contrib.auth.models import User


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='Wodka', slug='wodka')

    def test_category_model_entry(self):
        """
        Test Category model data 
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'Wodka')

    



class TestProductsModel(TestCase):

    def setUp(self):

        Category.objects.create(name='wodka2', slug='wodka2')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='wodka2', created_by_id=1,
                                            slug='wodka2', price='20.00', image='wodka22')
        self.data2 = Product.objects.create(category_id=1, title='grass', created_by_id=1,
                                             slug='grass', price='20.00', image='grass22', is_active=False)

    def test_products_model_entry(self):
        """
        Test product model data 
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'wodka2')

#     