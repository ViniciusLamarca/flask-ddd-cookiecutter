"""Run Flask application with WebSocket support."""
{% if cookiecutter.use_websocket == "y" %}
from app import create_app
from app.infrastructure.websocket.socketio import get_socketio

if __name__ == "__main__":
    app = create_app()
    socketio = get_socketio()
    
    # Run with SocketIO
    socketio.run(
        app,
        host="0.0.0.0",
        port=5000,
        debug=True,
        use_reloader=True,
    )
{% else %}
# WebSocket support is not enabled in this project.
# To enable it, regenerate the project with use_websocket="y"
print("WebSocket support is not enabled.")
{% endif %}

