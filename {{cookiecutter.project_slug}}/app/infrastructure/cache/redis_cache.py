"""Redis cache implementation."""
import json
import pickle
from typing import Any

from flask import current_app

from app.application.interfaces.cache import CacheInterface
{% if cookiecutter.include_redis == "y" %}
from app.infrastructure.redis.client import redis_client

import structlog

logger = structlog.get_logger()


class RedisCache(CacheInterface):
    """Redis implementation of cache interface."""
    
    def __init__(self, key_prefix: str = "cache:", serializer: str = "json") -> None:
        """
        Initialize Redis cache.
        
        Args:
            key_prefix: Prefix for all cache keys
            serializer: Serialization method ('json' or 'pickle')
        """
        self.key_prefix = key_prefix
        self.serializer = serializer
    
    def _get_client(self):
        """Get Redis client instance."""
        return redis_client.get_client()
    
    def _make_key(self, key: str) -> str:
        """
        Create full cache key with prefix.
        
        Args:
            key: Base key
        
        Returns:
            Prefixed key
        """
        return f"{self.key_prefix}{key}"
    
    def _serialize(self, value: Any) -> str | bytes:
        """
        Serialize value for storage.
        
        Args:
            value: Value to serialize
        
        Returns:
            Serialized value
        """
        if self.serializer == "json":
            return json.dumps(value)
        elif self.serializer == "pickle":
            return pickle.dumps(value)
        else:
            raise ValueError(f"Unknown serializer: {self.serializer}")
    
    def _deserialize(self, value: str | bytes) -> Any:
        """
        Deserialize value from storage.
        
        Args:
            value: Serialized value
        
        Returns:
            Deserialized value
        """
        if value is None:
            return None
        
        if self.serializer == "json":
            return json.loads(value)
        elif self.serializer == "pickle":
            return pickle.loads(value)
        else:
            raise ValueError(f"Unknown serializer: {self.serializer}")
    
    def get(self, key: str) -> Any | None:
        """
        Get value from cache.
        
        Args:
            key: Cache key
        
        Returns:
            Cached value or None if not found
        """
        try:
            full_key = self._make_key(key)
            value = self._get_client().get(full_key)
            
            if value is None:
                return None
            
            return self._deserialize(value)
        except Exception as e:
            logger.error("Cache get error", key=key, error=str(e))
            return None
    
    def set(self, key: str, value: Any, ttl: int | None = None) -> bool:
        """
        Set value in cache.
        
        Args:
            key: Cache key
            value: Value to cache
            ttl: Time to live in seconds (None for no expiration)
        
        Returns:
            True if successful, False otherwise
        """
        try:
            full_key = self._make_key(key)
            serialized = self._serialize(value)
            
            if ttl is not None:
                result = self._get_client().setex(full_key, ttl, serialized)
            else:
                result = self._get_client().set(full_key, serialized)
            
            return bool(result)
        except Exception as e:
            logger.error("Cache set error", key=key, error=str(e))
            return False
    
    def delete(self, key: str) -> bool:
        """
        Delete value from cache.
        
        Args:
            key: Cache key
        
        Returns:
            True if successful, False otherwise
        """
        try:
            full_key = self._make_key(key)
            result = self._get_client().delete(full_key)
            return result > 0
        except Exception as e:
            logger.error("Cache delete error", key=key, error=str(e))
            return False
    
    def exists(self, key: str) -> bool:
        """
        Check if key exists in cache.
        
        Args:
            key: Cache key
        
        Returns:
            True if key exists, False otherwise
        """
        try:
            full_key = self._make_key(key)
            return bool(self._get_client().exists(full_key))
        except Exception as e:
            logger.error("Cache exists error", key=key, error=str(e))
            return False
    
    def clear(self, pattern: str | None = None) -> int:
        """
        Clear cache entries.
        
        Args:
            pattern: Pattern to match keys (None to clear all with prefix)
        
        Returns:
            Number of keys deleted
        """
        try:
            client = self._get_client()
            
            if pattern is None:
                search_pattern = f"{self.key_prefix}*"
            else:
                search_pattern = f"{self.key_prefix}{pattern}"
            
            keys = client.keys(search_pattern)
            if keys:
                return client.delete(*keys)
            return 0
        except Exception as e:
            logger.error("Cache clear error", pattern=pattern, error=str(e))
            return 0
    
    def increment(self, key: str, amount: int = 1) -> int:
        """
        Increment a numeric value in cache.
        
        Args:
            key: Cache key
            amount: Amount to increment
        
        Returns:
            New value after increment
        """
        try:
            full_key = self._make_key(key)
            return self._get_client().incrby(full_key, amount)
        except Exception as e:
            logger.error("Cache increment error", key=key, error=str(e))
            raise
    
    def decrement(self, key: str, amount: int = 1) -> int:
        """
        Decrement a numeric value in cache.
        
        Args:
            key: Cache key
            amount: Amount to decrement
        
        Returns:
            New value after decrement
        """
        try:
            full_key = self._make_key(key)
            return self._get_client().decrby(full_key, amount)
        except Exception as e:
            logger.error("Cache decrement error", key=key, error=str(e))
            raise


# Global cache instance
cache: RedisCache | None = None


def get_cache() -> RedisCache:
    """
    Get cache instance.
    
    Returns:
        Cache instance
    
    Raises:
        RuntimeError: If cache is not initialized
    """
    global cache
    if cache is None:
        cache = RedisCache()
    return cache
{% else %}
# Redis is not enabled, cache functionality is not available
class RedisCache:
    """Placeholder when Redis is not enabled."""
    pass


def get_cache():
    """Placeholder when Redis is not enabled."""
    raise RuntimeError("Cache is not available. Redis must be enabled to use cache functionality.")
{% endif %}

