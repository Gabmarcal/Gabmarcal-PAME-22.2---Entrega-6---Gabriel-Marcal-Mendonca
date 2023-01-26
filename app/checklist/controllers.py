from flask import request
from flask.views import MethodView

from .models import Checklist
from .schemas import ChecklistSchema
from app.medicine.models import Medicine

class ChecklistController(MethodView):

    def get(self):
        schema=ChecklistSchema()
        checklist = Checklist.query.all()
        return schema.dump(checklist,many=True), 200

class ChecklistDetails(MethodView):

    def get(self,id_remedio):
        schema = ChecklistSchema()

        checklist = Checklist.query.get(id_remedio)

        if not checklist: return{}, 404

        return schema.dump(checklist), 200

    def post(self,id_remedio):
        schema = ChecklistSchema()

        medicine = Medicine.query.get(id_remedio)
        
        if not medicine: return{}, 404

        data = request.json

        data['id_remedio'] = medicine.id
        data['remedio'] = medicine.nome
        data['comprar'] = data['qnt_ideal'] - data['qnt_estoque']
        
        try:
            checklist = schema.load(data)
        except:
            return{}, 400
        
        checklist.save()

        return schema.dump(checklist), 201

class ChecklistUpdate(MethodView):

    def patch(self,id):
        schema = ChecklistSchema()

        checklist = Checklist.query.get(id)

        if not checklist: return{}, 404

        data = request.json
    
        try:
            checklist = schema.load(data, instance = checklist, partial=True)
        except:
            return{}, 400
        
        checklist.save()

        return schema.dump(checklist), 201
    
    def delete(self,id):
        checklist = Checklist.query.get(id)

        if not checklist: return{}, 404

        checklist.delete(checklist)
        return{}, 204