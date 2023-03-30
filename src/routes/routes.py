from src.controllers.controller import *

routes = {
    # "delete_route":"/delete/user/<int:id>", "deleteusercontroller":DeleteUserController.as_view("delete"),
    # "update_route":"/update/user/<int:id>", "updateusercontroller":UpdateUserController.as_view("update"),
    "index_route":"/", "indexcontroller":IndexController.as_view("index"),
}