from flask import Blueprint
from .controllers import *

checklist_api = Blueprint("checklist_api",__name__)

#/checklist
checklist_api.add_url_rule(

    "/checklist",
    view_func=ChecklistController.as_view("checklist_controller"),
    methods = ['GET']
)

#/checklist/id_remedio
checklist_api.add_url_rule(

    "/checklist/<int:id_remedio>",
    view_func=ChecklistDetails.as_view("checklist_details"),
    methods = ['GET','POST']
)

#/checklist/id
checklist_api.add_url_rule(

    "/checklist/<int:id>",
    view_func=ChecklistUpdate.as_view("checklist_update"),
    methods = ['PATCH','DELETE']
)