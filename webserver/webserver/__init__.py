from flask import Flask
from flask_cors import CORS
from logging.config import dictConfig

def init_app():
  """Initialize the core application."""
  app = Flask(__name__, instance_relative_config=False)
  CORS(app)
  app.config.from_object('config.Config')

  with app.app_context():
      # Include our Routes
      from .weather import routes as weather

      # Register Blueprints
      app.register_blueprint(weather.weather_bp)

      return app