from django.urls import path

from payment.views import stripe_webhook, order_placed
from . import views

app_name = 'orders'

urlpatterns = [
    path('add/', views.add, name='add'),
    path('orderplaced/', order_placed, name='order_placed'),
    # path('error/', views.Error.as_view(), name='error'),
    path('webhook/', stripe_webhook),
]
