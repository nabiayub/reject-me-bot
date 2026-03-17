from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: str
    webhook_url: str = "https://your-app.koyeb.app"  # Placeholder
    webhook_path: str = "/webhook"
    app_host: str = "0.0.0.0"
    port: int = 8000  # Automatically picks up PORT from environment (e.g., Render)
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


config = Settings()
