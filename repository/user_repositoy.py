import logging
from typing import Dict

from bson import ObjectId
from pymongo.errors import PyMongoError
from returns.result import Success, Failure, Result

from database.mongo_connect import users
from repository.logs_repository import logger_write


def insert_user(user: Dict):
    breakpoint()
    try:
        res = users.insert_one(user)
        return Success(res.inserted_id)
    except PyMongoError as e:
        return Failure(str(e))


def update_user(id_user: str, user: Dict):
    try:
        res = users.update_one({"_id": ObjectId(id_user)}, {"$set": user})
        return Success(res)
    except PyMongoError as e:
        return Failure(str(e))


def find_user(value: str):
    try:
        res = users.find_one({"_id": ObjectId(value)})
        return Success(res)
    except PyMongoError as e:
        return Failure(str(e))


def delete_user(user_id: str):
    try:
        res = users.delete_one({"_id": ObjectId(user_id)})
        return Success(res)
    except PyMongoError as e:
        return Failure(str(e))
def log_user(user:Result):
    breakpoint()
    message = "not success" if isinstance(user,Failure) else f"user is created successfully by id ${user}"
    logger_write(logging.INFO,message,"CREATE")
    return user



