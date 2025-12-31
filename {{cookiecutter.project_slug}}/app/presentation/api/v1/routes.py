"""API v1 routes."""
from flask import Blueprint, jsonify, render_template

api_bp = Blueprint("api_v1", __name__)


@api_bp.route("/health", methods=["GET"])
def health_check() -> dict:
    """
    Health check endpoint.
    
    Returns:
        Health status response
    """
    return jsonify({"status": "healthy", "service": "{{ cookiecutter.project_slug }}"})

