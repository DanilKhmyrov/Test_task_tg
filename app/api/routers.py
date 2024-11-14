from fastapi import APIRouter

from app.api.endpoints import exchange_transaction_router

main_router = APIRouter()
main_router.include_router(
    exchange_transaction_router,
    prefix='/exchange',
    tags=['exchange_transaction'])
