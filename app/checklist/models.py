from app.models import BaseModel
from app.extensions import db

class Checklist(BaseModel):
    __tablename__ = "checklist"

    id = db.Column(db.Integer, primary_key = True)
    remedio = db.Column(db.String(30), db.ForeignKey('medicine.nome'))
    id_remedio = db.Column(db.Integer, db.ForeignKey('medicine.id'))
    qnt_estoque = db.Column(db.Integer)
    qnt_ideal = db.Column(db.Integer)
    comprar = db.Column(db.Integer)