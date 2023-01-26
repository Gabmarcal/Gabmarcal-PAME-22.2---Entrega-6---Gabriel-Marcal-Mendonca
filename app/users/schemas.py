from app.extensions import ma
from .models import Users

class UserSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Users
        load_instance = True
        ordered = True

    
    id = ma.Integer(dump_only=True)
    username = ma.String(required=True)
    idade = ma.Integer(required=True)
    password = ma.String(required=True)

class LoginSchema(ma.Schema):

    username = ma.String(required=True)
    password = ma.String(load_only=True, required=True)