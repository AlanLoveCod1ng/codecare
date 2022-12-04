from datetime import datetime

from flask import abort, make_response


def get_timestamp():
    date = str(datetime.now())[0:10] + " " + str(datetime.now())[11:19]
    return date

DISEASE = {
    1: {
        "name": "Hepatitis A",
        "city": "Madison",
        "cases": 20,
        "content": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui.",
        "timestamp": get_timestamp(),
    },
    2: {
        "name": "Avian Influenza",
        "city": "Little Rock",
        "cases": 89,
        "content": "Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Fusce vulputate eleifend sapien. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Nullam accumsan lorem in dui. Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ac dui quis mi consectetuer lacinia.",
        "timestamp": get_timestamp(),
    },
    3: {
        "name": "Pneumococcal",
        "city": "Miami",
        "cases": 57,
        "content": "Nam pretium turpis et arcu. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis, ipsum. Sed aliquam ultrices mauris. Integer ante arcu, accumsan a, consectetuer eget, posuere ut, mauris. Praesent adipiscing. Phasellus ullamcorper ipsum rutrum nunc. Nunc nonummy metus. Vestibulum volutpat pretium libero. Cras id dui. Aenean ut eros et nisl sagittis vestibulum. Nullam nulla eros, ultricies sit amet, nonummy id, imperdiet feugiat, pede. Sed lectus. Donec mollis hendrerit risus. Phasellus nec sem in justo pellentesque facilisis. Etiam imperdiet imperdiet orci. Nunc nec neque. Phasellus leo dolor, tempus non, auctor et, hendrerit quis, nisi.",
        "timestamp": get_timestamp(),
    },
    4: {
        "name": "Measles",
        "city": "Newark",
        "cases": 85,
        "content": "Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet, leo. Maecenas malesuada. Praesent congue erat at massa. Sed cursus turpis vitae tortor. Donec posuere vulputate arcu. Phasellus accumsan cursus velit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed aliquam, nisi quis porttitor congue, elit erat euismod orci, ac placerat dolor lectus quis orci. Phasellus consectetuer vestibulum elit. Aenean tellus metus, bibendum sed, posuere ac, mattis non, nunc. Vestibulum fringilla pede sit amet augue. In turpis. Pellentesque posuere. Praesent turpis.",
        "timestamp": get_timestamp(),
    },
    5: {
        "name": "Tuberculosis",
        "city": "Newark",
        "cases": 54,
        "content": "Fusce convallis metus id felis luctus adipiscing. Pellentesque egestas, neque sit amet convallis pulvinar, justo nulla eleifend augue, ac auctor orci leo non est. Quisque id mi. Ut tincidunt tincidunt erat. Etiam feugiat lorem non metus. Vestibulum dapibus nunc ac augue. Curabitur vestibulum aliquam leo. Praesent egestas neque eu enim. In hac habitasse platea dictumst. Fusce a quam. Etiam ut purus mattis mauris sodales aliquam. Curabitur nisi. Quisque malesuada placerat nisl. Nam ipsum risus, rutrum vitae, vestibulum eu, molestie vel, lacus.",
        "timestamp": get_timestamp(),
    },
    6: {
        "name": "Tuberculosis",
        "city": "Paterson",
        "cases": 29,
        "content": "Morbi nec metus. Phasellus blandit leo ut odio. Maecenas ullamcorper, dui et placerat feugiat, eros pede varius nisi, condimentum viverra felis nunc et lorem. Sed magna purus, fermentum eu, tincidunt eu, varius ut, felis. In auctor lobortis lacus. Quisque libero metus, condimentum nec, tempor a, commodo mollis, magna. Vestibulum ullamcorper mauris at ligula. Fusce fermentum. Nullam cursus lacinia erat. Praesent blandit laoreet nibh.",
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
    content = disease.get("content")

    DISEASE[len(DISEASE) + 1] = {
            "name": name,
            "city": city,
            "cases": cases,
            "content": content,
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
