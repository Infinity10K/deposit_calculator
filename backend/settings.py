from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env", case_sensitive=True)

    def __getattr__(self, item):
        return self.__getattribute__(item)

    DATE_FORMAT: str = "%d.%m.%Y"
    PERIODS_MIN: int = 1
    PERIODS_MAX: int = 60
    RATE_MIN: float = 1
    RATE_MAX: float = 8
    AMOUNT_MIN: int = 10000
    AMOUNT_MAX: int = 3000000


settings = Settings()


print(settings.model_dump())
