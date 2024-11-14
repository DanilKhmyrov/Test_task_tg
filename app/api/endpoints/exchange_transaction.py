from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.schemas.exchange_transaction import ExchangeTransactionCreate, ExchangeTransactionDB, ExchangeTransactionResponse
from app.crud import exchange_transaction_crud


router = APIRouter()

SessionDep = Annotated[AsyncSession, Depends(get_async_session)]


@router.post(
    '/create',
    summary='Create a new exchange transaction',
    description='This endpoint allows creating a new exchange transaction by providing the necessary details. '
                'It returns a success message when the transaction is successfully created.',
    response_model=ExchangeTransactionResponse,
    status_code=201
)
async def create_exchange_transaction(
        transaction: ExchangeTransactionCreate,
        session: SessionDep):
    new_transaction = await exchange_transaction_crud.create(transaction, session)
    return {"status": "success", "message": "Exchange record created successfully"}


@router.get(
    '/{exchange_id}',
    summary='Get an exchange transaction by ID',
    description='This endpoint allows retrieving an exchange transaction using its unique `exchange_id`. '
                'It returns the transaction details, including status and other associated fields.',
    response_model=ExchangeTransactionDB,
    responses={
        404: {
            "description": "Transaction not found",
            "content": {
                "application/json": {
                    "example": {"message": "Transaction not found"}
                }
            }
        }
    }
)
async def get_exchange_transaction(
        exchange_id: int,
        session: SessionDep):
    transaction = await exchange_transaction_crud.get(exchange_id, session)
    return transaction
