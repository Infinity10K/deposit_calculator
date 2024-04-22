import pydantic
import datetime as dt

from settings import settings


class DepositIn(pydantic.BaseModel):
    date: str
    periods: int
    amount: int
    rate: float

    @pydantic.field_validator("date")
    def check_date_format(cls, v):
        try:
            return dt.datetime.strptime(v, settings.DATE_FORMAT).date()
        except ValueError:
            raise ValueError("Incorrect date format, should be dd.mm.YYYY")

    @pydantic.field_validator("periods")
    def validate_periods(cls, v):
        if not settings.PERIODS_MIN <= v <= settings.PERIODS_MAX:
            raise ValueError(
                f"Periods must be between {settings.PERIODS_MIN} and {settings.PERIODS_MAX}"
            )
        return v

    @pydantic.field_validator("rate")
    def validate_rate(cls, v):
        if not settings.RATE_MIN <= v <= settings.RATE_MAX:
            raise ValueError(
                f"Rate must be between {settings.RATE_MIN} and {settings.RATE_MAX}"
            )
        return v

    @pydantic.field_validator("amount")
    def validate_amount(cls, v):
        if not settings.AMOUNT_MIN <= v <= settings.AMOUNT_MAX:
            raise ValueError(
                f"Amount must be between {settings.AMOUNT_MIN} and {settings.AMOUNT_MAX}"
            )
        return v
