from flask import send_file
from flask_restplus import Namespace, Resource
import os

namespace = Namespace(
    "filtering", "Filtering phase in which we have the pre-processed data with plots"
)


@namespace.route("/boxplot")
class plot(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """Get filtering phase graphs"""
        ROOT_PATH = os.path.dirname(os.path.abspath("../image/test"))
        TRUE_PATH = os.path.join(ROOT_PATH, "nielie.jpg")
        return send_file(TRUE_PATH)
