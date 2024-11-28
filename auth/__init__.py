from flask import Flask
from flask_jwt_extended import JWTManager
from .auth import auth_bp

def init_app(app: Flask):
    # Registrar las rutas del Blueprint
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Configuración del secreto para firmar los JWT
    # app.config["JWT_SECRET_KEY"] = "mi_secreto_super_seguro"
    jwt = JWTManager(app)
