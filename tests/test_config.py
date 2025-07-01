from rescreener.config import Settings


def test_settings():
    settings = Settings()
    assert settings.testing_only == "Hello Test!"
