def userentity(item)-> dict:
    return {
        "_id":str(item["_id"]),
        "id": item["id"],
        "name": item["name"],
        "email": item["email"],
        "password": item["password"]
        
    }

def usersentity(entity)-> list:
    return [userentity(item) for item in entity]