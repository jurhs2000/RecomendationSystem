def serialize_user(user):
    return {
        "name": user.get("name"),
        "username": user.get("username"),
        "password": user.get("password"),
        "ingredients": []
    }

def serialize_ingredient(ingredient):
    return {
        "name": ingredient.get("name"),
        "tags": ingredient.get("tags")
    }

def serialize_meal(meal):
    return {
        "name": meal.get("name"),
        "tags": meal.get("tags"),
        "time": meal.get("time"),
        "rate": meal.get("rate"),
        "ingredients": [],
        "kinds": [],
        "styles": [],
        "tastes": [],
        "coincidence": 0.0
    }
