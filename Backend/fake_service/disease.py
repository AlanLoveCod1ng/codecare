from datetime import datetime

from flask import abort, make_response


def get_timestamp():
    return datetime.now().date()


DISEASE = {
    "Hepatitis A": {
        "name": "Hepatitis A",
        "state": "Lafayette",
        "cases": 20,
        "timestamp": get_timestamp(),
    },
    "Avian Influenza (Bird flu)": {
        "name": "Avian Influenza",
        "state": "Chicago",
        "cases": 89,
        "timestamp": get_timestamp(),
    },
    "Pneumococcal": {
        "name": "Pneumococcal",
        "state": "Miami",
        "cases": 57,
        "timestamp": get_timestamp(),
    },
    "fake": {
        "name": "fake",
        "state": "Seattle",
        "cases": 220,
        "timestamp": get_timestamp(),
    }
}


# DISEASE = [
#     {
#         "name": "Hepatitis A",
#         "state": "Wisconsin",
#         "cases": 20,
#         "timestamp": get_timestamp(),
#     },
#     {
#         "name": "Avian Influenza",
#         "state": "Wisconsin",
#         "cases": 20,
#         "timestamp": get_timestamp(),
#     },
#  {
#         "name": "Pneumococcal",
#         "state": "Wisconsin",
#         "cases": 20,
#         "timestamp": get_timestamp(),
#     },
#     {
#         "name": "fake",
#         "state": "hello",
#         "cases": 220,
#         "timestamp": get_timestamp(),
#     },
#     {
#         "name": "Hepatitis A",
#         "state": "hello",
#         "cases": 20,
#         "timestamp": get_timestamp(),
#     }
# ]



def read_all():
    return list(DISEASE.values())



# def create(disease):
#     name = disease.get("name")
#     state = disease.get("state")
#     cases = disease.get("cases")

#     if name not in DISEASE:
#         DISEASE[name] = {
#             "name": name,
#             "state": state,
#             "cases": cases,
#             "timestamp": get_timestamp(),
#         }
#         return DISEASE[name], 201
#     else:
#         abort(406, f"disease with the name {name} already exists")

# version2
def create(disease):
    name = disease.get("name")
    state = disease.get("state")
    cases = disease.get("cases")

    DISEASE[name] = {
            "name": name,
            "state": state,
            "cases": cases,
            "timestamp": get_timestamp(),
        }
    return DISEASE[name], 201



#state
def read_state(state):
    if state in DISEASE:
        return DISEASE[state]
    else:
        abort(404, f"no found")


def read_one(name):
    if name in DISEASE:
        return DISEASE[name]
    else:
        abort(404, f"disease with the name {name} not found")


def update(name, disease):
    if name in DISEASE:
        DISEASE[name]["state"] = disease.get("state")
        DISEASE[name]["cases"] = disease.get("cases")
        DISEASE[name]["timestamp"] = get_timestamp()
        return DISEASE[name]
    else:
        abort(404, f"disease with the name {name} not found")


def delete(name):
    if name in DISEASE:
        del DISEASE[name]
        return make_response(f"{name} successfully deleted", 200)
    else:
        abort(404, f"disease with the name {name} not found")
