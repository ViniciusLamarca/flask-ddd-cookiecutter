"""Cache interface - Abstract cache contract."""
from abc import ABC, abstractmethod
from typing import Any


class CacheInterface(ABC):
    """Interface for cache operations."""
    
    @abstractmethod
    def get(self, key: str) -> Any | None:
        """
        Get value from cache.
        
        Args:
            key: Cache key
        
        Returns:
            Cached value or None if not found
        """
        pass
    
    @abstractmethod
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
        pass
    
    @abstractmethod
    def delete(self, key: str) -> bool:
        """
        Delete value from cache.
        
        Args:
            key: Cache key
        
        Returns:
            True if successful, False otherwise
        """
        pass
    
    @abstractmethod
    def exists(self, key: str) -> bool:
        """
        Check if key exists in cache.
        
        Args:
            key: Cache key
        
        Returns:
            True if key exists, False otherwise
        """
        pass
    
    @abstractmethod
    def clear(self, pattern: str | None = None) -> int:
        """
        Clear cache entries.
        
        Args:
            pattern: Pattern to match keys (None to clear all)
        
        Returns:
            Number of keys deleted
        """
        pass
    
    @abstractmethod
    def increment(self, key: str, amount: int = 1) -> int:
        """
        Increment a numeric value in cache.
        
        Args:
            key: Cache key
            amount: Amount to increment
        
        Returns:
            New value after increment
        """
        pass
    
    @abstractmethod
    def decrement(self, key: str, amount: int = 1) -> int:
        """
        Decrement a numeric value in cache.
        
        Args:
            key: Cache key
            amount: Amount to decrement
        
        Returns:
            New value after decrement
        """
        pass

