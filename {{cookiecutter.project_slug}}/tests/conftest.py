"""Pytest configuration and fixtures."""
import pytest
from flask import Flask

from app import create_app
from app.infrastructure.database.session import db


@pytest.fixture
def app() -> Flask:
    """Create Flask application for testing."""
    app = create_app("testing")
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def client(app: Flask):
    """Create test client."""
    return app.test_client()


@pytest.fixture
def runner(app: Flask):
    """Create CLI test runner."""
    return app.test_cli_runner()

