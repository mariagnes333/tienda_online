from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    migrate = Migrate(app, db)

    # Importa los modelos
    from app.models.producto import Producto


    # Importa las rutas
    from .routes.producto_routes import producto_bp
    app.register_blueprint(producto_bp)

    from .routes.home_routes import home_bp
    app.register_blueprint(home_bp)
    
    return app
