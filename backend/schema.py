import pydantic
import datetime as dt

class DepositIn(pydantic.BaseModel):
    date: dt.date
    periods: int
    amount: int
    rate: float

