from flask import Blueprint
from .controllers import *

medicine_api = Blueprint("medicine_api",__name__)

#/medicine
medicine_api.add_url_rule(

    "/medicine",
    view_func=MedicineController.as_view("medicine_controller"),
    methods = ['POST','GET']
)

#/medicine/id
medicine_api.add_url_rule(

    "/medicine/<int:id>",
    view_func=MedicineDetails.as_view("medicine_details"),
    methods = ['GET','PUT','PATCH','DELETE']
)