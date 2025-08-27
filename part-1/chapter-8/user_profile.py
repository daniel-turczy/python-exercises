"""
Start with a copy of user_profile from page 148. Build a profile of yourself
by calling build_profile, using your first and last names and three other
key-value pairs that describe you.
"""

def build_profile(first, last, **user_info):
    """Return a dictionary with the user's first name, last name,
    and extra information."""
    profile = {
        "first_name": first,
        "last_name" : last
    }
    profile.update(user_info)
    return profile


person0 = build_profile(
    "franz", "liszt",
    age=54,
    height="185cm",
    nationality="hungarian"
)
print(person0)