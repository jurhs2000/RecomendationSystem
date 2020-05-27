def serialize_user(user):
    return {
        "name": user.get("name"),
        "username": user.get("username"),
        "password": user.get("password")
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
        "rate": meal.get("rate")
    }

def serialize_movie(movie):
    return {
        'id': movie['id'],
        'title': movie['title'],
        'summary': movie['summary'],
        'released': movie['released'],
        'duration': movie['duration'],
        'rated': movie['rated'],
        'tagline': movie['tagline']
    }

def serialize_cast(cast):
    return {
        'name': cast[0],
        'job': cast[1],
        'role': cast[2]
    }