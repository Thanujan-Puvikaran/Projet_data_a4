from flask_restplus import Namespace, Resource, fields
from config import raiseError
from mapping import defaultValue
import pickle
from flask import send_file
from hook import find_file

namespace = Namespace("model", "Model related endpoints")

payload = namespace.model(
    "model",
    {
        "Age": fields.Integer(
            description="Age: the value must be above 18, else there will be an error",
            required=False,
        ),
        "Gender": fields.String(
            description="Gender: if it is a male use 1 and female use 0. \nBy default it's a woman",
            required=True,
        ),
        "Education": fields.Float(
            description="""Education: \n
                        1 if he/she left school before 16 years
                        2 if he/she left school at 16 years
                        3 if he/she left school at 17 years
                        4 if he/she left school at 18 years
                        5 if he/she went to some college or university, no certificate or degree
                        6 if he/she has a professional certificate/ diploma
                        7 if he/she has a university degree
                        8 if he/she has a masters degree
                        9 if he/she has a doctorate degree""",
            required=False,
        ),
        "Nscore": fields.Integer(
            description="""Nscore: Neurotism score related to whether the patient has these characteristic: Anxiety, Angry/Hostility, Depression, Timidity, Impulsivity, Vulnerability 
            \nMark each of those from 0 to 10 and sum them before plugging them into the payload (the range of value is 12-60)""",
            required=False,
        ),
        "Escore": fields.Integer(
            description="""Escore: Extraversion level realted to Warmth/kindness, Gregariousness, Assertiveness, Activity, Excitment Seeking, Positive Emotion
            \nMark each of those from 0 to 10 and sum them before plugging them into the payload (the range of value is 16-59)""",
            required=False,
        ),
        "Oscore": fields.Integer(
            description="""Oscore: Open mindness level related to Fantasy, Aesthetics, Feelings, Actions, Ideas, Values/liberalism
            \nMark each of those from 0 to 10 and sum them before plugging them into the payload (the range of value is 24-60)""",
            required=False,
        ),
        "Ascore": fields.Integer(
            description="""Ascore: Agreeableness level related to Trust, Straightforwardness, Altruism, Compliance, Modesty, Tendermindedness
            \nMark each of those from 0 to 10 and sum them before plugging them into the payload (the range of value is 12-60)""",
            required=False,
        ),
        "Cscore": fields.Integer(
            description="""Cscore: Conscientiousness related to Competence, Order, Dutifulness, Achievement Striving, Self-Discipline, Deliberation
            \nMark each of those from 0 to 10 and sum them before plugging them into the payload (the range of value is 17-59)""",
            required=False,
        ),
        "SS": fields.Integer(
            description="""SS: Barrat Impulsiveness Test \nFactors: Attention, Cognitvity, Motor, Perseverance, Self-Control.
             \n(the range of value is 71-249)""",
            required=False,
        ),
        "Amphet": fields.Boolean(
            description="Amphet: whether the patient is using this drug (value: true or false)",
            required=False,
        ),
        "Amyl": fields.Boolean(
            description="Amyl: whether the patient is using this drug (value: true or false)",
            required=False,
        ),
        "Benzos": fields.Boolean(
            description="Benzos: whether the patient is using this drug (value: true or false)",
            required=False,
        ),
        "Cannabis": fields.Boolean(
            description="Cannabis: whether the patient is using this drug (value: true or false)",
            required=False,
        ),
        "Heroin": fields.Boolean(
            description="Heroin: whether the patient is using this drug (value: true or false)",
            required=False,
        ),
        "Ketamine": fields.Boolean(
            description="Ketamine: whether the patient is using this drug (value: true or false)",
            required=False,
        ),
        "LSD": fields.Boolean(
            description="LSD: whether the patient is using this drug (value: true or false)",
            required=False,
        ),
        "Meth": fields.Boolean(
            description="Meth: whether the patient is using this drug (value: true or false)",
            required=False,
        ),
        "VSA": fields.Boolean(
            description="VSA: whether the patient is using this drug (value: true or false)",
            required=False,
        ),
    },
)


@namespace.route("/knn")
class model(Resource):
    @namespace.doc(body=payload)
    @namespace.response(200, "Success")
    def post(self):
        """Predict the class of the consumer with knn method"""
        try:
            output_payload = defaultValue(payload=namespace.payload, flag=False)
            knn_filename = "../model/knn.pkl"
            with open(knn_filename, "rb") as file:
                knn_model = pickle.load(file)
            output = {"response": output_payload.value}
            # output = {"response": output_payload.value, "model": knn_model}
            # payload = defaultValue(payload=namespace.payload, flag=True)
            return output
        except Exception as e:
            if raiseError.JSONERROR in e.__str__():
                return {"response": {"error": raiseError.JSONMESSAGE}}
            elif raiseError.TYPEERROR in e.__str__():
                return {"response": {"error": raiseError.TYPEMESSAGE}}


@namespace.route("/knn/elbow")
class knn_elbow(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Get elbow method graph for the knn clustering """
        TRUE_PATH = find_file(fullname="Elbow_knn", extension=".png", path="../image/",)
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/knn/confusion_matrix")
class number_drug(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Get the Confusion Matrix for the knn method """
        TRUE_PATH = find_file(
            fullname="ConfusionMatrixKnn", extension=".png", path="../image/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)
