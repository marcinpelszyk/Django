from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from basket.basket import Basket
import stripe


@login_required
def BasketView(request):

    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')

    stripe.api_key = 'sk_test_51IkV3IA1ugarFvwDRuIVgraExBX4F5KvVWEh3d58NS0q8rDnCK01ES06uJ1tH1sHO5CAIrjj4UfAvJQvASs4taHE00UyQeTt9h'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='pln',
        metadata={'userid': request.user.id}
    )

    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})
