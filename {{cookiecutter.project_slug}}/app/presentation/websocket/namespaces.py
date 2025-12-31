"""WebSocket namespaces."""
from flask_socketio import Namespace, emit
from typing import Any

import structlog

logger = structlog.get_logger()


class DefaultNamespace(Namespace):
    """Default WebSocket namespace."""
    
    def on_connect(self) -> None:
        """
        Handle client connection.
        
        Emits:
            connected: Connection confirmation message
        """
        logger.info("Client connected", session_id=self.request.sid)
        emit("connected", {"message": "Connected to server", "session_id": self.request.sid})
    
    def on_disconnect(self) -> None:
        """
        Handle client disconnection.
        """
        logger.info("Client disconnected", session_id=self.request.sid)
    
    def on_ping(self) -> None:
        """
        Handle ping from client.
        
        Emits:
            pong: Pong response
        """
        logger.debug("Ping received", session_id=self.request.sid)
        emit("pong", {"message": "pong"})
    
    def on_custom_event(self, data: dict[str, Any]) -> None:
        """
        Example custom event handler.
        
        Args:
            data: Event data from client
        
        Emits:
            custom_response: Response to custom event
        """
        logger.info("Custom event received", data=data, session_id=self.request.sid)
        emit("custom_response", {"received": data, "message": "Event processed"})


def register_namespaces(socketio: Any) -> None:
    """
    Register WebSocket namespaces.
    
    Args:
        socketio: SocketIO instance
    """
    socketio.on_namespace(DefaultNamespace("/"))
    logger.info("WebSocket namespaces registered")

