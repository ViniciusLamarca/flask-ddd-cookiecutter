"""Cache decorators for function result caching."""
import hashlib
import inspect
from functools import wraps
from typing import Any, Callable

{% if cookiecutter.include_redis == "y" %}
from app.infrastructure.cache.redis_cache import get_cache

import structlog

logger = structlog.get_logger()


def cached(ttl: int | None = None, key_prefix: str | None = None) -> Callable:
    """
    Decorator to cache function results.
    
    Args:
        ttl: Time to live in seconds (None for no expiration)
        key_prefix: Prefix for cache key (default: function name)
    
    Returns:
        Decorated function
    
    Example:
        @cached(ttl=300)
        def expensive_operation(user_id: int) -> dict:
            # This result will be cached for 5 minutes
            return {"data": "expensive computation"}
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            cache = get_cache()
            
            # Generate cache key
            if key_prefix is None:
                prefix = f"{func.__module__}.{func.__name__}"
            else:
                prefix = key_prefix
            
            # Create key from function arguments
            key_parts = [prefix]
            if args:
                key_parts.append(str(args))
            if kwargs:
                # Sort kwargs for consistent key generation
                sorted_kwargs = sorted(kwargs.items())
                key_parts.append(str(sorted_kwargs))
            
            key_string = ":".join(key_parts)
            # Hash long keys to keep them manageable
            if len(key_string) > 200:
                key_hash = hashlib.md5(key_string.encode()).hexdigest()
                cache_key = f"{prefix}:{key_hash}"
            else:
                cache_key = key_string
            
            # Try to get from cache
            cached_value = cache.get(cache_key)
            if cached_value is not None:
                logger.debug("Cache hit", key=cache_key, function=func.__name__)
                return cached_value
            
            # Cache miss - execute function
            logger.debug("Cache miss", key=cache_key, function=func.__name__)
            result = func(*args, **kwargs)
            
            # Store in cache
            cache.set(cache_key, result, ttl=ttl)
            
            return result
        
        return wrapper
    return decorator


def cache_key(key_pattern: str, ttl: int | None = None) -> Callable:
    """
    Decorator to cache function results with a custom key pattern.
    
    Args:
        key_pattern: Cache key pattern (can use {arg_name} placeholders)
        ttl: Time to live in seconds (None for no expiration)
    
    Returns:
        Decorated function
    
    Example:
        @cache_key("user:{user_id}:profile", ttl=600)
        def get_user_profile(user_id: int) -> dict:
            return {"user_id": user_id, "profile": "..."}
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            cache = get_cache()
            
            # Get function signature
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            # Format cache key with arguments
            try:
                cache_key = key_pattern.format(**bound_args.arguments)
            except KeyError as e:
                logger.warning(
                    "Cache key pattern error",
                    pattern=key_pattern,
                    error=str(e),
                    function=func.__name__
                )
                # Fallback to function execution without caching
                return func(*args, **kwargs)
            
            # Try to get from cache
            cached_value = cache.get(cache_key)
            if cached_value is not None:
                logger.debug("Cache hit", key=cache_key, function=func.__name__)
                return cached_value
            
            # Cache miss - execute function
            logger.debug("Cache miss", key=cache_key, function=func.__name__)
            result = func(*args, **kwargs)
            
            # Store in cache
            cache.set(cache_key, result, ttl=ttl)
            
            return result
        
        return wrapper
    return decorator


def invalidate_cache(key_pattern: str) -> Callable:
    """
    Decorator to invalidate cache entries after function execution.
    
    Args:
        key_pattern: Cache key pattern to invalidate (can use {arg_name} placeholders)
    
    Returns:
        Decorated function
    
    Example:
        @invalidate_cache("user:{user_id}:profile")
        def update_user_profile(user_id: int, data: dict) -> dict:
            # This will invalidate the cache for this user's profile
            return update_profile(user_id, data)
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Execute function first
            result = func(*args, **kwargs)
            
            # Invalidate cache
            cache = get_cache()
            
            # Get function signature
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            # Format cache key with arguments
            try:
                cache_key = key_pattern.format(**bound_args.arguments)
                cache.delete(cache_key)
                logger.debug("Cache invalidated", key=cache_key, function=func.__name__)
            except KeyError as e:
                logger.warning(
                    "Cache invalidation pattern error",
                    pattern=key_pattern,
                    error=str(e),
                    function=func.__name__
                )
            
            return result
        
        return wrapper
    return decorator
{% else %}
# Redis is not enabled, cache decorators are not available
def cached(*args: Any, **kwargs: Any) -> Callable:
    """Placeholder when Redis is not enabled."""
    def decorator(func: Callable) -> Callable:
        return func
    return decorator


def cache_key(*args: Any, **kwargs: Any) -> Callable:
    """Placeholder when Redis is not enabled."""
    def decorator(func: Callable) -> Callable:
        return func
    return decorator


def invalidate_cache(*args: Any, **kwargs: Any) -> Callable:
    """Placeholder when Redis is not enabled."""
    def decorator(func: Callable) -> Callable:
        return func
    return decorator
{% endif %}

