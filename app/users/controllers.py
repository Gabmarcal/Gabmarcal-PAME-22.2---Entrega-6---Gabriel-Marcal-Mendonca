from flask import request
from flask.views import MethodView

from .models import Users
from .schemas import UserSchema, LoginSchema

from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

class UserController(MethodView):
    
    def post(self):
        schema = UserSchema()
        data = request.json

        try:
            user = schema.load(data)
        except:
            return{}, 400
        
        user.save()

        return schema.dump(user), 201
    
    def get(self):
        schema=UserSchema()
        users = Users.query.all()
        return schema.dump(users,many=True), 200

class UserDetails(MethodView):

    decorators = [jwt_required()]

    def get(self,id):
        schema = UserSchema()

        user = Users.query.get(id)

        if id!=get_jwt_identity(): return{}, 401

        if not user: return{}, 404

        return schema.dump(user), 200
    
    def put(self,id):
        schema = UserSchema()

        user = Users.query.get(id)

        if not user: return{}, 404

        data = request.json
        try:
            user = schema.load(data, instance = user)
        except:
            return{}, 400
        
        user.save()

        return schema.dump(user), 201
    
    def patch(self,id):
        schema = UserSchema()

        user = Users.query.get(id)

        if not user: return{}, 404

        data = request.json
        try:
            user = schema.load(data, instance = user, partial=True)
        except:
            return{}, 400
        
        user.save()

        return schema.dump(user), 201
    
    def delete(self,id):
        user = Users.query.get(id)

        if not user: return{}, 404

        user.delete(user)
        return{}, 204

class UserLogin(MethodView):

    def post(self):
        schema = LoginSchema()
        data = schema.load(request.json)

        user = Users.query.filter_by(username=data['username']).first()

        if not user: return{}, 404

        if not user.check_password(data['password']): return{}, 401

        token = create_access_token(identity=user.id)

        return {"user": UserSchema().dump(user), "token": token}, 200