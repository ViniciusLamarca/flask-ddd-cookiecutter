"""Flask-SocketIO configuration and setup."""
from typing import Any

from flask import Flask
from flask_socketio import SocketIO

import structlog

logger = structlog.get_logger()

# Global SocketIO instance
socketio: SocketIO | None = None


def init_socketio(app: Flask) -> SocketIO:
    """
    Initialize Flask-SocketIO with Flask application.
    
    Args:
        app: Flask application instance
    
    Returns:
        SocketIO instance
    """
    global socketio
    
    # Get configuration from app config
    cors_allowed_origins = app.config.get("SOCKETIO_CORS_ALLOWED_ORIGINS", "*")
    async_mode = app.config.get("SOCKETIO_ASYNC_MODE", "eventlet")
    logger_enabled = app.config.get("SOCKETIO_LOGGER", app.config.get("DEBUG", False))
    engineio_logger_enabled = app.config.get("SOCKETIO_ENGINEIO_LOGGER", app.config.get("DEBUG", False))
    
    socketio = SocketIO(
        app,
        cors_allowed_origins=cors_allowed_origins,
        async_mode=async_mode,
        logger=logger_enabled,
        engineio_logger=engineio_logger_enabled,
        ping_timeout=app.config.get("SOCKETIO_PING_TIMEOUT", 60),
        ping_interval=app.config.get("SOCKETIO_PING_INTERVAL", 25),
    )
    
    logger.info(
        "SocketIO initialized",
        async_mode=async_mode,
        cors_allowed_origins=cors_allowed_origins,
    )
    
    return socketio


def get_socketio() -> SocketIO:
    """
    Get SocketIO instance.
    
    Returns:
        SocketIO instance
    
    Raises:
        RuntimeError: If SocketIO is not initialized
    """
    if socketio is None:
        raise RuntimeError("SocketIO not initialized. Call init_socketio() first.")
    return socketio

