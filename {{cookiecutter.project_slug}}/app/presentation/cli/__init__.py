"""CLI commands registration."""
from flask import Flask

from app.presentation.cli.commands import register_commands


def register_cli_commands(app: Flask) -> None:
    """
    Register CLI commands with Flask application.
    
    Args:
        app: Flask application instance
    """
    register_commands(app)

