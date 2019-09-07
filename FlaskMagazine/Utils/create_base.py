from FlaskMagazine.database import init_db
from FlaskMagazine.database import db_session
from FlaskMagazine.models import Product, Feature

init_db()

p = Product('Смартфон Xiaomi',1)
p1 = Product('Смартфон Sumsung',2)
p2 = Product('Смартфон Nokia',3)

db_session.add(p)
db_session.add(p1)
db_session.add(p2)
db_session.commit()

for i in range(1,4):
    f = Feature('Тип', 'Смартфон', i)
    f1 = Feature('Операционная система', 'Android', i)
    f2 = Feature('Тип корпуса', 'классический', i)

    db_session.add(f)
    db_session.add(f1)
    db_session.add(f2)
    db_session.commit()
