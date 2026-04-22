from .models import Payment
import uuid
from sqlalchemy.orm import Session
from .stripe_client import create_payment_intent


def create_payment(
    session: Session, amount: int, currency: str, user_id: str
) -> Payment:
    intent = create_payment_intent(amount, currency)

    payment = Payment(
        id=str(uuid.uuid4()),
        amount=amount,
        currency=currency,
        user_id=user_id,
        stripe_payment_id=intent["id"],
        status=intent["status"],
    )

    session.add(payment)
    session.commit()

    return payment
