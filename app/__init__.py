from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Blueprint
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from app.models import db
from flask import Flask
from app.routes.routes import routes_bp
import app
routes_bp = Blueprint(
    'routes_bp' , __name__,
    template_folder = 'templates',
    static_folder = 'static'

)

def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    db.init_app(app)

    with app.app_context():

        app.register_blueprint(routes_bp)

        db.create_all()



    return app

