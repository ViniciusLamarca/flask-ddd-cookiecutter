"""WebSocket event handlers."""
from flask_socketio import emit
from typing import Any

import structlog

logger = structlog.get_logger()


def register_events(socketio: Any) -> None:
    """
    Register WebSocket event handlers.
    
    Args:
        socketio: SocketIO instance
    """
    
    @socketio.on("connect")
    def handle_connect() -> None:
        """Handle client connection."""
        logger.info("Client connected via event handler")
        emit("connected", {"message": "Connected to server"})
    
    @socketio.on("disconnect")
    def handle_disconnect() -> None:
        """Handle client disconnection."""
        logger.info("Client disconnected")
    
    @socketio.on("message")
    def handle_message(data: dict[str, Any]) -> None:
        """
        Handle text message from client.
        
        Args:
            data: Message data
        """
        logger.info("Message received", data=data)
        emit("message", {"echo": data, "message": "Message received"})
    
    @socketio.on("json")
    def handle_json(json: dict[str, Any]) -> None:
        """
        Handle JSON message from client.
        
        Args:
            json: JSON data
        """
        logger.info("JSON received", json=json)
        emit("json", {"echo": json, "message": "JSON received"})
    
    logger.info("WebSocket events registered")

