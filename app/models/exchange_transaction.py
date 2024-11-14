from enum import Enum
import time

from sqlalchemy import BigInteger, String, Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class TransactionStatus(str, Enum):
    initial = 'initial'
    paid = 'paid'


class ExchangeTransaction(Base):
    status: Mapped[TransactionStatus] = mapped_column(
        SqlEnum(TransactionStatus),
        default=TransactionStatus.initial,
        nullable=False
    )
    receive_currency: Mapped[str] = mapped_column(String(10), nullable=False)
    send_currency: Mapped[str] = mapped_column(String(10), nullable=False)
    receive_network: Mapped[str] = mapped_column(String(50), nullable=False)
    send_network: Mapped[str] = mapped_column(String(50), nullable=False)
    receive_address: Mapped[str] = mapped_column(String(100), nullable=False)
    exchange_id: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False)
    created_at: Mapped[int] = mapped_column(
        BigInteger, default=int(time.time()))
