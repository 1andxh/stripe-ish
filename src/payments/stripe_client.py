import stripe
from ..config import settings

stripe.api_key = settings.STRIPE_API_KEY


def create_payment_intent(amount: int, currency: str):
    return stripe.PaymentIntent.create(amount=amount, currency=currency)
