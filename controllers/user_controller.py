from flask import blueprints, request

from repository.user_repositoy import find_user, insert_user, log_user
from utils.json_unit import parse_json

user_blueprints = blueprints.Blueprint("/api/user", __name__)


@user_blueprints.route("/<string:id>", methods=["GET"])
def get_user(id: str):
    res = find_user(id)

    return (res
            .map(lambda u: (parse_json(u), 200))
            .value_or((parse_json({}), 404))
            )


@user_blueprints.route("/create", methods=["POST"])
def post_user():
    return (insert_user(request.json)
            .map(log_user)
            .map(lambda u: (parse_json(u), 200))
            .value_or((parse_json({}), 404))
            )
