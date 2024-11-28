from flask_cors import CORS

def init_cors(app):
    """
    Configura CORS para la aplicación Flask.
    """
    CORS(app, resources={r"/api/*": {
        "origins": ["https://mi-sitio.com"],
        "methods": ["POST"],
        "allow_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True
    }})
