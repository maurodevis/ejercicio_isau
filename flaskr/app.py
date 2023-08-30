from flaskr import create_app
from .modelos import db, Usuario, Album, Medio

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
    u = Usuario(nombre='mauricio', contrasena='mao123')
    a = Album(titulo="blessed ovi", anio='2023', descripcion='canciones de bleesd y otro artitas', medio=Medio.CD)
    u.albumes.append(a)
    db.session.add(u)
    db.session.commit()
    print(Usuario.query.all())
    print(Usuario.query.all()[0].albumes)
    db.session.delete(u)
    print(Usuario.query.all())
    print(Album.query.all())

