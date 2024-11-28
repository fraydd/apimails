from flask import Blueprint, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

# Configuración del Blueprint
auth_bp = Blueprint('auth', __name__)

# Ruta para login y creación del JWT
@auth_bp.route("/login", methods=["POST"])
def login():
    # Obtener los datos de login (usuario y contraseña) desde el cuerpo de la solicitud
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    # Validación simple (puedes integrarlo con un sistema de base de datos)
    if username != "admin" or password != "password123":  # Solo un ejemplo
        return jsonify({"msg": "Credenciales incorrectas"}), 401

    # Crear un JWT
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

# Ruta protegida por JWT
@auth_bp.route("/protected", methods=["GET"])
@jwt_required()  # Esta ruta requiere un token válido
def protected():
    # Obtener la identidad del token JWT (usuario autenticado)
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
