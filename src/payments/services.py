from .models import Payment, PaymentStatus
import uuid
from sqlalchemy.orm import Session


def create_payment(
    session: Session, amount: int, currency: str, user_id: str
) -> Payment:
    payment_id = str(uuid.uuid4())

    payment = Payment(
        id=payment_id,
        amount=amount,
        currency=currency,
        user_id=user_id,
        status=PaymentStatus.PENDING,
    )

    session.add(payment)
    session.commit()
