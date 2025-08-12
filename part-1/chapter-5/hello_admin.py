"""
Make a list of five or more usernames, including "admin".
Imagine you are writing code that will print a greeting to each user after
they log in to a website. Loop through the list, and print a greeting to
each user.

- If the username is "admin", print a special greeting.
- Otherwise, print a generic greeting.
"""

usernames = [
    "admin"
    "dan",
    "patrick",
    "christian",
    "nathan"
]

if usernames:
    for username in usernames:
        if username == "admin":
            print(f"Hello {username.title()}, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thanks for logging in.")
else:
    print("We need to get some users!")