from flask_restplus import Namespace, Resource, fields
import pandas as pd
import os

namespace = Namespace("dataset", "Dataset related endpoints")

dataset_model = namespace.model(
    "dataset", {"data": fields.Raw(readonly=True, description="dataset columns")},
)


@namespace.route("/columns")
class dataset(Resource):
    @namespace.marshal_list_with(dataset_model)
    @namespace.response(200, "Success")
    def get(self):
        """Get dataset columns name"""
        ROOT_PATH = os.path.dirname(
            os.path.abspath("../Projet/Analyse_Exploratoire/data_preproc.csv")
        )
        df = pd.read_csv(os.path.join(ROOT_PATH, "data_preproc.csv"))
        print(df.columns)
        output = {"data": {i: df.columns[i] for i in range(len(df.columns))}}
        return output
