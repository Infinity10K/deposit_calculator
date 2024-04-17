from fastapi import FastAPI
import datetime as dt
from dateutil.relativedelta import relativedelta

from schema import DepositIn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.post("/deposit")
async def deposit(deposit: DepositIn):
    result = {}
    amount = deposit.amount
    for i in range(deposit.periods):
        date = deposit.date + relativedelta(months=i)
        amount = amount * (1 + deposit.rate / 100 / 12)
        result.update({
            date.strftime("%d.%m.%Y"): round(amount, 2),
        })
    return result