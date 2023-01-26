from app.extensions import ma
from .models import Checklist

class ChecklistSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Checklist
        load_instance = True
        ordered = True

    
    id = ma.Integer(dump_only=True)
    id_remedio = ma.Integer(required=True)
    remedio = ma.String(required=True)
    qnt_estoque = ma.Integer(required=True)
    qnt_ideal = ma.Integer(required=True)
    comprar = ma.Integer(required=True)