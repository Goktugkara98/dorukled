# -*- coding: utf-8 -*-
import os
import sys
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask
from flask_talisman import Talisman
# Import the blueprint from the routes file
from app.routes.main_routes import main
from app.models.db import init_db


def create_app():
    app = Flask(__name__,
                static_folder='static',
                template_folder='templates')

    # Load configuration
    # Assuming config.py is in the root directory, one level above src
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.py')
    example_config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.example.py')

    if os.path.exists(config_path):
        app.config.from_pyfile(config_path)
        print(f"Loaded configuration from {config_path}")
    elif os.path.exists(example_config_path):
        app.config.from_pyfile(example_config_path)
        print(f"Loaded configuration from {example_config_path}")
    else:
        # Default fallback configuration if neither file exists
        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key_change_me')
        print("Warning: config.py or config.example.py not found. Using default settings.")

    # Initialize HTTPS with Talisman (as per original app)
    # Note: content_security_policy=None might need review for production security
    # Talisman(app, content_security_policy=None, force_https=False)

    # Initialize Database
    init_db(app)

    # Register blueprints
    app.register_blueprint(main)

    return app

app = create_app()

if __name__ == '__main__':
    # Ensure the app runs on 0.0.0.0 to be accessible externally
    # Debug should be False in production
    port = int(os.environ.get('PORT', 5001))
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')
    app.run(host='0.0.0.0', port=port, debug=True)
