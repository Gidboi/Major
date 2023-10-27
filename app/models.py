from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import db
import app
db = SQLAlchemy()
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120))
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, email, name, password, is_admin=False):
        self.email = email
        self.name = name
        self.password = password
        self.is_admin = is_admin


with app.app_context():
    db.create_all()
    admin_user = User.query.filter_by(email='gidbois029@gmail.com').first()
    if not admin_user:
        admin_user = User(email='gidbois029@gmail.com', name='Admin',
                          password='d09154c8b29a10d6f8f91ff9d4487c2731187dcb62660575d0e2e32007d6ca91',
                          is_admin=True)
        db.session.add(admin_user)
        db.session.commit()