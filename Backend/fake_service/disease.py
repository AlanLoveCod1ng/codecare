from datetime import datetime

from flask import abort, make_response


def get_timestamp():
    return datetime.now().date()


DISEASE = {
    1: {
        "name": "Hepatitis A",
        "state": "Lafayette",
        "cases": 20,
        "timestamp": get_timestamp(),
    },
    2: {
        "name": "Avian Influenza",
        "state": "Chicago",
        "cases": 89,
        "timestamp": get_timestamp(),
    },
    3: {
        "name": "Pneumococcal",
        "state": "Miami",
        "cases": 57,
        "timestamp": get_timestamp(),
    },
    4: {
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



# version2
def create(disease):
    name = disease.get("name")
    state = disease.get("state")
    cases = disease.get("cases")

    DISEASE[len(DISEASE) + 1] = {
            "name": name,
            "state": state,
            "cases": cases,
            "timestamp": get_timestamp(),
        }
    return DISEASE[len(DISEASE)], 201



#state
def read_state(state):
    if state in DISEASE:
        return DISEASE[state]
    else:
        abort(404, f"no found")


# get the list of specific type of disease
def read_one(name):
    ret_list = []
    for i in DISEASE:

        if DISEASE[i]['name'] == name:
    
            print(DISEASE[i]['name'])

            ret_list.append(DISEASE[i])

    return ret_list



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
