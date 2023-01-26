from flask import Blueprint
from .controllers import *

user_api = Blueprint("user_api",__name__)

#/users
user_api.add_url_rule(

    "/users",
    view_func=UserController.as_view("users_controller"),
    methods = ['POST','GET']
)

#/users/id
user_api.add_url_rule(

    "/users/<int:id>",
    view_func=UserDetails.as_view("users_details"),
    methods = ['GET','PUT','PATCH','DELETE']
)

#/login
user_api.add_url_rule(

    "/login",
    view_func=UserLogin.as_view("users_login"),
    methods = ['POST']
)