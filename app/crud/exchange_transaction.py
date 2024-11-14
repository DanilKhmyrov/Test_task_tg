from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import CRUDBase
from app.models import ExchangeTransaction, TransactionStatus


class CRUDExchangeTransaction(CRUDBase):

    async def get_transactions_by_status(
            self,
            status: TransactionStatus,
            session: AsyncSession):
        result = await session.execute(
            select(ExchangeTransaction)
            .where(ExchangeTransaction.status == status))
        return result.scalars().all()


exchange_transaction_crud = CRUDExchangeTransaction(ExchangeTransaction)
