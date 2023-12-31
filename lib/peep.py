class Peep:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, posted_on, peep, user_name, user_id):
        self.id = id
        self.posted_on = posted_on
        self.peep = peep
        self.user_name = user_name
        self.user_id = user_id

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Peep({self.id}, {self.posted_on}, {self.peep}, {self.user_name}, {self.user_id})"

    # These next two methods will be used by the controller to check if
    # books are valid and if not show errors to the user.
    # def is_valid(self):
    #     if self.title == None or self.title == "":
    #         return False
    #     if self.author_name == None or self.author_name == "":
    #         return False
    #     return True

    # def generate_errors(self):
    #     errors = []
    #     if self.title == None or self.title == "":
    #         errors.append("Title can't be blank")
    #     if self.author_name == None or self.author_name == "":
    #         errors.append("Author name can't be blank")
    #     if len(errors) == 0:
    #         return None
    #     else:
    #         return ", ".join(errors)
