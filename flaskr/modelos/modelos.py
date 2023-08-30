from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
import enum

db = SQLAlchemy()

albumes_canciones = db.Table('album_cancion',
    db.Column('album_id', db.Integer, db.ForeignKey('album.id'), primary_key=True),
    db.Column('cancion_id', db.Integer, db.ForeignKey('cancion.id'), primary_key=True))


class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))



class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    contrasena = db.Column(db.Integer)
    albumes = db.relationship("Album", cascade="all, delete, delete-orphan")

class Medio(enum.Enum):
    DISCO = 1
    CASETE = 2
    CD = 3


class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150))
    anio = db.Column(db.Integer)
    descripcion = db.Column(db.String(100))
    medio = db.Column(db.Enum(Medio))
    usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    __tables_args__ = (db.UniqueConstraint("usuario","titulo", name="titulo_unico_album"),)


class EnumADiccionario(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return {"llave":value.name, "valor":value.value}

class AlbumSchema(SQLAlchemyAutoSchema):
    medio=EnumADiccionario(attribute=("medio"))
    class Meta:
        model = Album
        include_relationships = True
        load_instance = True

class CancionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Cancion
        include_relationships = True
        load_instance = True

class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        include_relationships = True
        load_instance = True