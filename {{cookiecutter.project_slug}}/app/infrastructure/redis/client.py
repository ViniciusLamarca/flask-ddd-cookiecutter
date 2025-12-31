"""Redis client configuration."""
from typing import Any

import redis
from flask import Flask


class RedisClient:
    """Redis client wrapper for Flask application."""
    
    def __init__(self) -> None:
        """Initialize Redis client."""
        self.client: redis.Redis[Any] | None = None
    
    def init_app(self, app: Flask) -> None:
        """
        Initialize Redis client with Flask app configuration.
        
        Args:
            app: Flask application instance
        """
        config = app.config
        
        self.client = redis.Redis(
            host=config.get("REDIS_HOST", "localhost"),
            port=config.get("REDIS_PORT", 6379),
            password=config.get("REDIS_PASSWORD"),
            db=config.get("REDIS_DB", 0),
            decode_responses=config.get("REDIS_DECODE_RESPONSES", True),
        )
        
        # Test connection
        try:
            self.client.ping()
            app.logger.info("Redis connection established")
        except redis.ConnectionError as e:
            app.logger.error(f"Redis connection failed: {e}")
            raise
    
    def get_client(self) -> redis.Redis[Any]:
        """
        Get Redis client instance.
        
        Returns:
            Redis client instance
        
        Raises:
            RuntimeError: If client is not initialized
        """
        if self.client is None:
            raise RuntimeError("Redis client not initialized. Call init_app() first.")
        return self.client


redis_client = RedisClient()

