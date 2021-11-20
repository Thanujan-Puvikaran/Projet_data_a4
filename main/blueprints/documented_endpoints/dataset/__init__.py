from flask_restplus import Namespace, Resource, fields
import pandas as pd
import os

namespace = Namespace("dataset", "Dataset related endpoints")

dataset_model = namespace.model(
    "dataset", {"data": fields.Raw(readonly=True, description="dataset columns")},
)


@namespace.route("/base/columns")
class basic_dataset(Resource):
    @namespace.marshal_list_with(dataset_model)
    @namespace.response(200, "Success")
    def get(self):
        """Get the basic dataset columns name"""
        ROOT_PATH = os.path.dirname(
            os.path.abspath("../Projet/Analyse_Exploratoire/data_preproc.csv")
        )
        df = pd.read_csv(os.path.join(ROOT_PATH, "data_preproc.csv"))
        print(df.columns)
        output = {"data": {i: df.columns[i - 1] for i in range(1, len(df.columns) + 1)}}
        return output


@namespace.route("/processed/columns")
class final_dataset(Resource):
    # @namespace.marshal_list_with(dataset_model)
    @namespace.response(200, "Success")
    def get(self):
        """Get the final dataset columns name"""
        ROOT_PATH = os.path.dirname(os.path.abspath("../Projet/Models/data_tofit.csv"))
        df = pd.read_csv(os.path.join(ROOT_PATH, "data_tofit.csv"))
        print(df.columns)
        output = {"data": {i: df.columns[i - 1] for i in range(1, len(df.columns) + 1)}}
        return output
