from pydantic import Field
from pydantic_settings import BaseSettings


class SettingsPostgres(BaseSettings):

    DB_USERNAME: str
    DB_PASSWORD: str
    DB_PORT: str
    DB_HOST: str
    DB_BASENAME: str

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"

    @property
    def dsn(self):
        return "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
            self.DB_USERNAME,
            self.DB_PASSWORD,
            self.DB_HOST,
            self.DB_PORT,
            self.DB_BASENAME
        )


settings_pg = SettingsPostgres()
