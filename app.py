from flask import Flask, jsonify, request
from middlewares.cors import init_cors
from auth import init_app as init_auth
from dotenv import load_dotenv
from flask_jwt_extended import jwt_required 
import os

load_dotenv()
app = Flask(__name__)

# Inicializar middleware CORS
init_cors(app)

# Configurar la app usando las variables de entorno
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["FLASK_ENV"] = os.getenv("FLASK_ENV")

# Inicializar las rutas de autenticación
init_auth(app)

# Ruta GET para obtener un saludo
@app.route('/api/saludo', methods=['GET'])
@jwt_required()
def saludo():
    return jsonify({"mensaje": "¡Hola!"})


if __name__ == '__main__':
    app.run(debug=True)
