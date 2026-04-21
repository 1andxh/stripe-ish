from sqlalchemy import String, Integer, Enum as SAEnum
from sqlalchemy.orm import mapped_column, Mapped
from src.database import Base
import enum


class PaymentStatus(str, enum.Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    amount: Mapped[int]
    currency: Mapped[str]
    user_id: Mapped[str]
    status: Mapped[PaymentStatus]
    stripe_payment_id: Mapped[str] = mapped_column(String, nullable=True)
