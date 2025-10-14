def validate_title(title):
    if not title or len(title) < 3:
        raise ValueError("Title must be at least 3 characters long.")
    return title

def validate_description(description):
    if description and len(description) > 200:
        raise ValueError("Description must be 200 characters or less.")
    return description