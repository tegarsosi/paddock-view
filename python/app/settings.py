from pydantic_settings import BaseSettings, SettingsConfigDict
from yarl import URL


class Settings(BaseSettings):
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def db_url(self) -> str:
        return str(
            URL.build(
                scheme="postgres",
                user=self.db_user,
                password=self.db_password,
                host=self.db_host,
                port=self.db_port,
                path=f"/{self.db_name}",
            ),
        )


settings = Settings()
