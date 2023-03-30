from flask import Flask, render_template, request, url_for, redirect
from src.routes.routes import *

app = Flask(__name__)

app.add_url_rule(routes["index_route"], view_func=routes["indexcontroller"])

# app.add_url_rule(routes["delete_route"], view_func=routes["deleteusercontroller"])

# app.add_url_rule(routes["update_route"], view_func=routes["updateusercontroller"])