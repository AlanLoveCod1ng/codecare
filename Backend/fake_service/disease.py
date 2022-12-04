from datetime import datetime

from flask import abort, make_response


def get_timestamp():
    return datetime.now().date()


DISEASE = {
    1: {
        "name": "Hepatitis A",
        "city": "Madison",
        "cases": 20,
        "timestamp": get_timestamp(),
    },
    2: {
        "name": "Avian Influenza",
        "city": "Little Rock",
        "cases": 89,
        "timestamp": get_timestamp(),
    },
    3: {
        "name": "Pneumococcal",
        "city": "Miami",
        "cases": 57,
        "timestamp": get_timestamp(),
    },
    4: {
        "name": "Measles",
        "city": "Newark",
        "cases": 85,
        "timestamp": get_timestamp(),
    },
    5: {
        "name": "Tuberculosis",
        "city": "Newark",
        "cases": 54,
        "timestamp": get_timestamp(),
    },
    6: {
        "name": "Tuberculosis",
        "city": "Paterson",
        "cases": 29,
        "timestamp": get_timestamp(),
    }
}


# DISEASE = [
#     {
#         "name": "Hepatitis A",
#         "city": "Wisconsin",
#         "cases": 20,
#         "timestamp": get_timestamp(),
#     },
#     {
#         "name": "Avian Influenza",
#         "city": "Wisconsin",
#         "cases": 20,
#         "timestamp": get_timestamp(),
#     },
#  {
#         "name": "Pneumococcal",
#         "city": "Wisconsin",
#         "cases": 20,
#         "timestamp": get_timestamp(),
#     },
#     {
#         "name": "fake",
#         "city": "hello",
#         "cases": 220,
#         "timestamp": get_timestamp(),
#     },
#     {
#         "name": "Hepatitis A",
#         "city": "hello",
#         "cases": 20,
#         "timestamp": get_timestamp(),
#     }
# ]



def read_all():
    return list(DISEASE.values())



# version2
def create(disease):
    name = disease.get("name")
    city = disease.get("city")
    cases = disease.get("cases")

    DISEASE[len(DISEASE) + 1] = {
            "name": name,
            "city": city,
            "cases": cases,
            "timestamp": get_timestamp(),
        }
    return DISEASE[len(DISEASE)], 201



#city
def read_state(city):
    if city in DISEASE:
        return DISEASE[city]
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
        DISEASE[name]["city"] = disease.get("city")
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
