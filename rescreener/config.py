"""A module to define configurations used by pydantic-settings"""

from pydantic_settings import BaseSettings, SettingsConfigDict

__all__ = ["Settings"]

class Settings(BaseSettings):
    """A class to define configurations used by pydantic-settings"""
    # do NOT change these values as they impact on tests/test_config.py
    host: str = "0.0.0.0"
    port: int = 80
    # do not change this value as it impacts on "tests/test_config.py"
    testing_only: str = "Hello Test!"
    # to allow overriding from .env if found.
    model_config = SettingsConfigDict(env_file=".env")
