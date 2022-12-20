class User:
    # define attributes of the class
    name = "No Name Provided"
    email = ""
    password = "123abcd"
    account = 0

    # Define the methods of the class
    def login(self):
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("You are not authorized for this page.")
# Outside of the class you would create an instance of the User class
new_user = User()
# Call the login method using the new object
new_user.login()