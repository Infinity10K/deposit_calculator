from dateutil.relativedelta import relativedelta
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError

from schema import DepositIn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# 422 handler
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError):
    str_exc = ", ".join(
        f"{error.get('loc')} - {error.get('msg')}" for error in exc.errors()
    )
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"error": str_exc}),
    )


@app.post("/deposit")
async def deposit(deposit: DepositIn):
    result = {}
    amount = deposit.amount
    for i in range(deposit.periods):
        date = deposit.date + relativedelta(months=i)
        amount = amount * (1 + deposit.rate / 100 / 12)
        result.update(
            {
                date.strftime("%d.%m.%Y"): round(amount, 2),
            }
        )
    return result
