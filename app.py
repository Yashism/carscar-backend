# app.py

from flask import Flask
from api import api_bp
from auth import auth_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["*", "https://sub.example.com"])

# Register blueprints
app.register_blueprint(api_bp)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run()
