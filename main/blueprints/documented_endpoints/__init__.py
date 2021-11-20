from flask import Blueprint
from flask_restplus import Api
from blueprints.documented_endpoints.dataset import namespace as dataset_ns
from blueprints.documented_endpoints.analyse_exploratoire import namespace as image_ns
from blueprints.documented_endpoints.model import namespace as models_ns


blueprint = Blueprint("api", __name__, url_prefix="/v1")

api_extension = Api(
    blueprint,
    title="PROJECT A4 DATA ANALYSIS",
    version="1.0",
    description="Api to present the results of our data analysis and ou model",
    doc="/documentation",
)

api_extension.add_namespace(dataset_ns)
api_extension.add_namespace(image_ns)
api_extension.add_namespace(models_ns)
