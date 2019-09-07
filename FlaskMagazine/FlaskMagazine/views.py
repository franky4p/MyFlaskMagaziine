"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskMagazine import app
from werkzeug.exceptions import NotFound
from FlaskMagazine.database import db_session
from FlaskMagazine.models import Product, Feature

PRODUCTS = {1:'Tablet', 2:'Phone', 3:'Laptop'}
pro = [{'name':'tipo name', 'value':'tipo model'},
      {'name':'tipo name1', 'value':'tipo model1'},
       ]

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    products = Product.query.all()
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        products=products
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Контакты',
        year=datetime.now().year,
        message='Контактные данные'
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='О сайте',
        year=datetime.now().year,
        message='Мой первый сайт на Flask'
    )


@app.route('/<int:id>', endpoint='product')
def product(id=None):
    """Renders the product page."""
    title = Product.query.filter(Product.id == id).first()
    if not title:
        raise NotFound(f'Product #{id} does not exist')

    product_details = Feature.query.filter(Feature.id_product == id).all()

    return render_template(
        'product.html',
        title=title.name,
        year=datetime.now().year,
        details=product_details,
        id=id
        )


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()