from flask_restplus import Namespace, Resource, fields

namespace = Namespace("models", "Model related endpoints")

model = namespace.model(
    "models", {"models": fields.Raw(readonly=True, description="modeling")},
)


@namespace.route("/model")
class model(Resource):
    @namespace.marshal_list_with(model)
    @namespace.response(200, "Success")
    def post(self):
        """"""
        pass
