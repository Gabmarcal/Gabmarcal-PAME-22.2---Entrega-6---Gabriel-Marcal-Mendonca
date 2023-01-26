from app.models import BaseModel
from app.extensions import db

class Medicine(BaseModel):
    __tablename__ = "medicine"

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(30))
    prescricao = db.Column(db.String(30))
    fabricante = db.Column(db.String(30))
    validade = db.Column(db.String(30))