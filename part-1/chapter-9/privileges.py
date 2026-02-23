class User:
    """A user with basic personal information."""
    
    def __init__(self, f_name, l_name, age):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """Print a message with the user's full name and age."""
        message = f"{self.f_name} {self.l_name} is {self.age} years old."
        print(message)

    def greet_user(self):
        """Print a personalised greeting."""
        message = f"Hello {self.f_name}. It's good to see you."
        print(message)

    def increment_login_attempts(self):
        """Increase the login_attempts attribute by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Set the login_attempts attribute to 0."""
        self.login_attempts = 0


class Admin(User):
    """
    An admin with basic personal information and privileges.
    Subclass to User.
    """

    def __init__(self, f_name, l_name, age):
        """
        Initialize attributes from User superclass and then 
        initialize admin privileges.
        """
        super().__init__(f_name, l_name, age)
        self.privileges = Privileges()
        
        
class Privileges():
    """Privileges for an admin. Works with the Admin class."""
    def __init__(self):
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can disable server",
            "can enable server"
        ]

    def show(self):
        """Print the admin's privileges."""
        print("---PRIVILEGES---")
        for priv in self.privileges:
            print(f"- {priv}")