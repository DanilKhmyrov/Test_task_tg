from pydantic import BaseModel, ConfigDict, Field


class ExchangeTransactionBase(BaseModel):
    receive_currency: str = Field(..., min_length=1)
    send_currency: str = Field(..., min_length=1)
    receive_network: str = Field(..., min_length=1)
    send_network: str = Field(..., min_length=1)
    receive_address: str = Field(..., min_length=1)
    exchange_id: str = Field(..., min_length=1)

    model_config = ConfigDict(from_attributes=True)


class ExchangeTransactionCreate(ExchangeTransactionBase):
    pass


class ExchangeTransactionDB(ExchangeTransactionBase):
    status: str
    created_at: int


class ExchangeTransactionResponse(BaseModel):
    status: str
    message: str

    model_config = ConfigDict(
        extra='forbid',
        json_schema_extra={
            "example": {
                "status": "success",
                "message": "Exchange record created successfully"
            }
        }
    )
