from flask import Blueprint
from flask_restplus import Api
from blueprints.documented_endpoints.dataset import namespace as dataset_ns


blueprint = Blueprint("api", __name__, url_prefix="/v1")

api_extension = Api(
    blueprint,
    title="PROJECT A4 DATA ANALYSIS",
    version="1.0",
    description="Api to present the results of our data analysis",
    doc="/documentation",
)

api_extension.add_namespace(dataset_ns)
