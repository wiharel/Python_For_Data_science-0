import math


def NULL_not_found(object: any) -> int:
    type_names = {
        None: "Nothing",
        math.nan: "Cheese",
        '0': "Zero",
        '': "Empty",
        False: "Fake"
    }

    i = 0
    type_names = type_names.get(object, "Type not found")
    if type_names == "Type not found":
        i = 1

    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif type(object) is float:
        print(f"Cheese {object} {type(object)}")
    elif type(object) is int and object == 0:
        print(f"Zero: {object} {type(object)}")
    elif object == '':
        print(f"Empty: {type(object)} {object}")
    elif type(object) is str and type_names != "Type not found":
        print(f"{type(object)}: {object}")
    elif type(object) is bool and not object:
        print(f"Fake: {object} {type(object)} ")
    else:
        print("Type not found")
    if i == 1:
        return 1
    return 0
