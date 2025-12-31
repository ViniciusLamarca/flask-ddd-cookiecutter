"""Error handling middleware."""
from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

import structlog

logger = structlog.get_logger()


def register_error_handlers(app: Flask) -> None:
    """
    Register error handlers for Flask application.
    
    Args:
        app: Flask application instance
    """
    
    @app.errorhandler(HTTPException)
    def handle_http_exception(e: HTTPException) -> tuple[dict, int]:
        """
        Handle HTTP exceptions.
        
        Args:
            e: HTTP exception
        
        Returns:
            Error response and status code
        """
        logger.error("HTTP error", status_code=e.code, description=e.description)
        return jsonify({"error": e.description, "status_code": e.code}), e.code
    
    @app.errorhandler(Exception)
    def handle_generic_exception(e: Exception) -> tuple[dict, int]:
        """
        Handle generic exceptions.
        
        Args:
            e: Exception
        
        Returns:
            Error response and status code
        """
        logger.exception("Unhandled exception", error=str(e))
        return jsonify({"error": "Internal server error", "status_code": 500}), 500

