from flask import request
from flask.views import MethodView

from .models import Medicine
from .schemas import MedicineSchema

class MedicineController(MethodView):
    
    def post(self):
        schema = MedicineSchema()
        data = request.json

        try:
            medicine = schema.load(data)
        except:
            return{}, 400
        
        medicine.save()

        return schema.dump(medicine), 201
    
    def get(self):
        schema=MedicineSchema()
        medicine = Medicine.query.all()
        return schema.dump(medicine,many=True), 200

class MedicineDetails(MethodView):

    def get(self,id):
        schema = MedicineSchema()

        medicine = Medicine.query.get(id)

        if not medicine: return{}, 404

        return schema.dump(medicine), 200

    
    def put(self,id):
        schema = MedicineSchema()

        medicine = Medicine.query.get(id)

        if not medicine: return{}, 404

        data = request.json
        try:
            medicine = schema.load(data, instance = medicine)
        except:
            return{}, 400
        
        medicine.save()

        return schema.dump(medicine), 201
    
    def patch(self,id):
        schema = MedicineSchema()

        medicine = Medicine.query.get(id)

        if not medicine: return{}, 404

        data = request.json
        try:
            medicine = schema.load(data, instance = medicine, partial=True)
        except:
            return{}, 400
        
        medicine.save()

        return schema.dump(medicine), 201
    
    def delete(self,id):
        medicine = Medicine.query.get(id)

        if not medicine: return{}, 404

        medicine.delete(medicine)
        return{}, 204