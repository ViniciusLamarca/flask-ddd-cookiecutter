"""Structured logging setup with structlog."""
import logging
import sys
from typing import Any

import structlog
from flask import Flask


def setup_logging(app: Flask) -> None:
    """
    Configure structured logging with structlog.
    
    Args:
        app: Flask application instance
    """
    # Configure structlog
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.StackInfoRenderer(),
            structlog.dev.set_exc_info,
            structlog.processors.format_exc_info,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.dev.ConsoleRenderer() if app.config.get("DEBUG") else structlog.processors.JSONRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=False,
    )
    
    # Configure standard logging
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=logging.DEBUG if app.config.get("DEBUG") else logging.INFO,
    )
    
    # Get logger
    logger = structlog.get_logger()
    logger.info("Logging configured", environment=app.config.get("ENV", "development"))

