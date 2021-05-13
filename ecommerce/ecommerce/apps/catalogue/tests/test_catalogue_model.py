import pytest 
from django.urls import reverse


def test_catalogue_model_category_str(product_category):
    assert product_category.__str__() == "Oleje"

def test_category_reverse(client, product_category):
    category = product_category
    url = reverse("catalogue:category_list", args=[category.slug])
    response = client.get(url)
    assert response.status_code == 200

