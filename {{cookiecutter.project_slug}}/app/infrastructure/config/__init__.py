"""Configuration management with Dynaconf."""
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="FLASK",
    settings_files=["app/infrastructure/config/settings.toml"],
    environments=True,
    load_dotenv=True,
    env_switcher="FLASK_ENV",
)

