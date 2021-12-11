from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify

namespace = Namespace("model", "Model related endpoints")

model = namespace.model(
    "model",
    {
        "prediction": fields.Raw(
            readonly=True,
            description="Use this endpoint in order to predict the type of consumer",
        )
    },
)
payload = namespace.model(
    "model",
    {"age": fields.Integer(description="Age of the person"), "name": fields.String},
)


@namespace.route("")
class model(Resource):
    @namespace.doc(body=payload)
    @namespace.marshal_list_with(model)
    @namespace.response(200, "Success")
    def post(self):
        """Predict the class of the consumer"""
        payload = namespace.payload
        output = {"prediction": payload}
        return output
