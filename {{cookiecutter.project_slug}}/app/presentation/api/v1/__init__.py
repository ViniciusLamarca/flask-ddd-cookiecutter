"""API v1 routes."""
from flask import Flask, render_template

from app.presentation.api.v1.routes import api_bp


def register_routes(app: Flask) -> None:
    """
    Register API routes with Flask application.
    
    Args:
        app: Flask application instance
    """
    # Register API blueprint
    app.register_blueprint(api_bp, url_prefix="/api/v1")
    
    # Register welcome page route
    @app.route("/")
    def welcome() -> str:
        """
        Welcome landing page.
        
        Returns:
            Welcome page HTML
        """
        return render_template("welcome.html")

