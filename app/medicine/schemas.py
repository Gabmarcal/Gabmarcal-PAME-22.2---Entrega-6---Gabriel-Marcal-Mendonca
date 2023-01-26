from app.extensions import ma
from .models import Medicine

class MedicineSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Medicine
        load_instance = True
        ordered = True

    
    id = ma.Integer(dump_only=True)
    nome = ma.String(required=True)
    prescricao = ma.String(required=True)
    fabricante = ma.String(required=True)
    validade = ma.String(required=True)