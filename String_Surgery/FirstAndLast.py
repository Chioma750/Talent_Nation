def first_and_last(value):
    if value == "":
        return {"first": "", "last": ""}
        
    diction = {
        "first": value[0],
        "last": value[-1],
    }
    return diction
    
print(first_and_last("python"))