"""Flask application factory with DDD and Clean Architecture."""
from flask import Flask
from dynaconf import FlaskDynaconf

from app.infrastructure.config import settings
from app.infrastructure.database.session import db
from app.infrastructure.logging.setup import setup_logging
from app.presentation.api.v1 import register_routes
from app.presentation.middleware.error_handler import register_error_handlers

{% if cookiecutter.include_redis == "y" %}
from app.infrastructure.redis.client import redis_client
{% endif %}
{% if cookiecutter.include_websocket == "y" %}
from app.infrastructure.websocket.socketio import init_socketio, get_socketio
from app.presentation.websocket.namespaces import register_namespaces
from app.presentation.websocket.events import register_events
{% endif %}


def create_app(config_name: str | None = None) -> Flask:
    """
    Create and configure Flask application.
    
    Args:
        config_name: Configuration environment name (development, testing, production)
    
    Returns:
        Configured Flask application instance
    """
    app = Flask(
        __name__,
        template_folder="presentation/templates",
        static_folder="presentation/static"
    )
    
    # Initialize Dynaconf
    FlaskDynaconf(app, settings_files=["app/infrastructure/config/settings.toml"])
    
    # Setup logging
    setup_logging(app)
    
    # Initialize database
    db.init_app(app)
    
    {% if cookiecutter.include_redis == "y" %}
    # Initialize Redis
    redis_client.init_app(app)
    {% endif %}
    
    {% if cookiecutter.include_websocket == "y" %}
    # Initialize WebSocket
    socketio = init_socketio(app)
    register_namespaces(socketio)
    register_events(socketio)
    {% endif %}
    
    # Register error handlers
    register_error_handlers(app)
    
    # Register API routes
    register_routes(app)
    
    # Register CLI commands
    from app.presentation.cli import register_cli_commands
    register_cli_commands(app)
    
    return app

