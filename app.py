import logging

from flask import Flask

from controllers.user_controller import user_blueprints
from repository.logs_repository import setup_log_index, logger_write
app = Flask(__name__)
app.register_blueprint(user_blueprints,url_prefix= "/api/user")

if __name__ == '__main__':
   setup_log_index()
   logger_write(logging.INFO, "Starting the app", "main")
   app.run()