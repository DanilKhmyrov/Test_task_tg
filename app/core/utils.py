import asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import TransactionStatus
from app.crud import exchange_transaction_crud
from app.core import logger


async def update_transaction_statuses(session: AsyncSession):
    """
    Background task for updating the status of transactions in the database.

    This process runs every minute and checks for records in the database with
    the status 'initial'. If such records are found, their status is updated to 'paid'.
    """

    while True:
        try:
            logger.info('Starting to check for transactions with "initial" status.')
            initial_transactions = await exchange_transaction_crud.get_transactions_by_status(
                TransactionStatus.initial, session
            )

            if not initial_transactions:
                logger.info('No transactions found with "initial" status.')
                await asyncio.sleep(60)
                continue

            for transaction in initial_transactions:
                logger.info(f'Updating status of exchange_id {transaction.exchange_id} to "paid"')
                transaction.status = TransactionStatus.paid
                session.add(transaction)

            await session.commit()
            logger.info('Transactions statuses updated successfully.')

        except Exception as e:
            logger.error(f'Error while updating transaction statuses: {e}')

        await asyncio.sleep(60)
