from sqlalchemy import Column, Integer, String
from FlaskMagazine.database import Base


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)

    def __init__(self, name=None, id=None):
        self.name = name
        self.id = id

    def __repr__(self):
        return '<Product %r>' % (self.name)


class Feature(Base):
    __tablename__ = 'feature'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=False)
    value = Column(String(50), unique=False)
    id_product = Column(Integer)

    def __init__(self, name=None, value=None, id_product=None):
        self.name = name
        self.value = value
        self.id_product = id_product

    def __repr__(self):
        return '<Feature %r>' % (self.name)