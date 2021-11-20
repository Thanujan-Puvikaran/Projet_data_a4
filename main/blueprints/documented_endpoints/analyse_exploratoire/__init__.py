from flask import send_file
from flask_restplus import Namespace, Resource, fields
from hook import find_file

namespace = Namespace(
    "filtering",
    "Filtering phase in which we have the plots which we use in order to do the pre processing",
)


@namespace.route("/pieplot")
class target_composition(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Get pieplot with target composition """
        TRUE_PATH = find_file(
            fullname="target_composition", extension=".png", path="../image/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/boxplot/addiction/education")
class Education_vs_Target(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Get the boxplot for education in function of addiction """
        TRUE_PATH = find_file(
            fullname="Education_vs_Target", extension=".png", path="../image/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/boxplot/addiction/age")
class Age_vs_Target(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Get the boxplot for age in function of addiction """
        TRUE_PATH = find_file(
            fullname="Age_vs_Target", extension=".png", path="../image/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/boxplot/addiction/ethnicity")
class Ethnicity_vs_Target(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Get the boxplot for ethnicity in function of addiction """
        TRUE_PATH = find_file(
            fullname="Ethnicity_vs_Target", extension=".png", path="../image/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/boxplot/addiction/gender")
class Gender_vs_Target(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Get the boxplot for Gender in function of addiction """
        TRUE_PATH = find_file(
            fullname="Gender_vs_Target", extension=".png", path="../image/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/boxplot/addiction/escore")
class Escore_vs_Target(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Get the boxplot for escore in function of addiction """
        TRUE_PATH = find_file(
            fullname="Escore_vs_Target", extension=".png", path="../image/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/boxplot/addiction/nscore")
class Nscore_vs_Target(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Get the boxplot for nscore in function of addiction """
        TRUE_PATH = find_file(
            fullname="NScore_vs_Target", extension=".png", path="../image/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/boxplot/addiction/oscore")
class Oscore_vs_Target(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Get the boxplot for oscore in function of addiction """
        TRUE_PATH = find_file(
            fullname="Oscore_vs_Target", extension=".png", path="../image/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/boxplot/addiction/cscore")
class Cscore_vs_Target(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Get the boxplot for cscore in function of addiction """
        TRUE_PATH = find_file(
            fullname="Cscore_vs_Target", extension=".png", path="../image/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/boxplot/addiction/ascore")
class Ascore_vs_Target(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Get the boxplot for ascore in function of addiction """
        TRUE_PATH = find_file(
            fullname="Ascore_vs_Target", extension=".png", path="../image/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/boxplot/addiction/impulsiveness")
class Impulsiveness_vs_Target(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Get the boxplot for impulsiveness in function of addiction """
        TRUE_PATH = find_file(
            fullname="Impulsive_vs_Target", extension=".png", path="../image/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/boxplot/addiction/ss")
class SS_vs_Target(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Get the boxplot for ss in function of addiction """
        TRUE_PATH = find_file(
            fullname="SS_vs_Target", extension=".png", path="../image/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/boxplot/drugs/nscore")
class nscore_drugs(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Get the boxplot for nscore in function of drugs """
        TRUE_PATH = find_file(
            fullname="NScore_drugs", extension=".png", path="../image/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/boxplot/drugs/escore")
class escore_drugs(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Get the boxplot for escore in function of drugs """
        TRUE_PATH = find_file(
            fullname="Escore_drugs", extension=".png", path="../image/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/boxplot/drugs/oscore")
class oscore_drugs(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Get the boxplot for oscore in function of drugs """
        TRUE_PATH = find_file(
            fullname="Oscore_drugs", extension=".png", path="../image/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/boxplot/drugs/cscore")
class cscore_drugs(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Get the boxplot for cscore in function of drugs """
        TRUE_PATH = find_file(
            fullname="Cscore_drugs", extension=".png", path="../image/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/boxplot/drugs/ascore")
class ascore_drugs(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Get the boxplot for ascore in function of drugs """
        TRUE_PATH = find_file(
            fullname="Ascore_drugs", extension=".png", path="../image/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/boxplot/drugs/impulsiveness")
class impulsive_drugs(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Get the boxplot for impulsiveness in function of drugs """
        TRUE_PATH = find_file(
            fullname="Impulsive_drugs", extension=".png", path="../image/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/boxplot/addiction/number_drug")
class number_drug(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Get the boxplot for the number of drug in function of addiction """
        TRUE_PATH = find_file(
            fullname="nbDrug_vs_Target", extension=".png", path="../image/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)

