def all_thing_is_obj(object: any) -> int:
    object_type = type(object)
    type_names = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
    }

    if object_type in type_names:
        print(f"{type_names[object_type]} : {object_type}")
    elif object_type is str:
        print(f"{object} is in the kitchen : {object_type}")
    else:
        print("Type not found")

    return 42
