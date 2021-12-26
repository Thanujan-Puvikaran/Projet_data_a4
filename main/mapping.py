import numpy as np


class defaultValue:
    """replace empty string or 0 by default value, here it's NaN"""

    DEFAULTVALUE = {"Age": -0.95197, "Education": -2.43591}

    def __init__(self, payload, flag=False):
        self.default(payload, flag)
        self.default_bool()
        self.gender()
        self.age()
        self.education()

    def default(self, payload, flag=False):
        if flag:
            self.value = {
                key: (np.NaN if value == "string" or value == 0 else value)
                for key, value in payload.items()
            }
        else:
            self.value = {
                key: ("" if value == "string" else value)
                for key, value in payload.items()
            }

    def default_bool(self):
        for key, val in self.value.items():
            if type(val) == bool:
                self.value[key] = 1 if val == True else 0

    def age(self):
        if self.value["Age"] >= 18 and self.value["Age"] <= 24:
            self.value["Age"] = -0.95197
        elif self.value["Age"] >= 25 and self.value["Age"] <= 34:
            self.value["Age"] = -0.07854
        elif self.value["Age"] >= 35 and self.value["Age"] <= 44:
            self.value["Age"] = 0.49788
        elif self.value["Age"] >= 45 and self.value["Age"] <= 54:
            self.value["Age"] = 1.09449
        elif self.value["Age"] >= 55 and self.value["Age"] <= 64:
            self.value["Age"] = 1.82213
        elif self.value["Age"] >= 65:
            self.value["Age"] = 2.59171
        else:
            self.value["Age"] = self.DEFAULTVALUE["Age"]

    def gender(self):
        self.value["Gender"] = (
            -0.48246
            if self.value["Gender"] in "malMmMalMalemale" and self.value["Gender"] != ""
            else 0.48246
        )

    def education(self):
        if self.value["Education"] == 1:
            self.value["Education"] = -2.43591
        elif self.value["Education"] == 2:
            self.value["Education"] = -1.73790
        elif self.value["Education"] == 3:
            self.value["Education"] = -1.43719
        elif self.value["Education"] == 4:
            self.value["Education"] = -1.22751
        elif self.value["Education"] == 5:
            self.value["Education"] = -0.61113
        elif self.value["Education"] == 6:
            self.value["Education"] = -0.05921
        elif self.value["Education"] == 7:
            self.value["Education"] = 0.45468
        elif self.value["Education"] == 8:
            self.value["Education"] = 1.16365
        elif self.value["Education"] == 9:
            self.value["Education"] = 1.98437
        else:
            self.value["Education"] = self.DEFAULTVALUE["Education"]

    def nscore(self):
        pass

    def escore(self):
        pass

    def oscore(self):
        pass

    def ascore(self):
        pass

    def cscore(self):
        pass

    def ss(self):
        pass
