"""Configuration management with Dynaconf."""
import os
from pathlib import Path
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="FLASK",
    settings_files=["app/infrastructure/config/settings.toml"],
    environments=True,
    load_dotenv=True,
    env_switcher="FLASK_ENV",
)

# Fallback to SQLite in development if DATABASE_URL is not set or empty
if settings.current_env == "development":
    # Check if DATABASE_URL env var exists and is not empty
    env_database_url = os.getenv("DATABASE_URL", "").strip()
    if not env_database_url:
        # Get database_url from settings (already loaded from env or settings.toml)
        database_url = settings.get("database_url", "").strip()
        # If still empty or just the placeholder, use SQLite as fallback
        if not database_url or database_url == "@env DATABASE_URL":
            # Use SQLite as fallback in development
            # Database file will be created in the project root
            project_root = Path(__file__).parent.parent.parent.parent
            sqlite_db_path = project_root / "local.db"
            sqlite_url = f"sqlite:///{sqlite_db_path}"
            settings.set("database_url", sqlite_url)
            settings.set("DATABASE_URL", sqlite_url)

