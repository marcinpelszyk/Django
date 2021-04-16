from django.test import TestCase
from django.urls import reverse
from shop.models import Category, Product
from django.contrib.auth.models import User


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='Wodka', slug='wodka')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'Wodka')

    # def test_category_url(self):
    #     """
    #     Test category model slug and URL reverse
    #     """
    #     data = self.data1
    #     response = self.client.post(
    #         reverse('shop:all_products', args=[data.slug]))
    #     self.assertEqual(response.status_code, 200)



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
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'wodka2')

#     def test_products_url(self):
#         """
#         Test product model slug and URL reverse
#         """
#         data = self.data1
#         url = reverse('shop:product_detail', args=[data.slug])
#         self.assertEqual(url, '/item/wokda2/')
#         response = self.client.post(
#             reverse('shop:product_detail', args=[data.slug]))
#         self.assertEqual(response.status_code, 200)

#     def test_products_custom_manager_basic(self):
#         """
#         Test product model custom manager returns only active products
#         """
#         data = Product.objects.all()
#         self.assertEqual(data.count(), 1)