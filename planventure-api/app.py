from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import environ
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL', 'sqlite:///planventure.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)

    # Register routes
    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to PlanVenture API"})

    @app.route('/health')
    def health_check():
        return jsonify({"status": "healthy"})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)