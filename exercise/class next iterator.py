class Users:
    active_users = []
    total_users = 0

    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
        Users.active_users.append({"name": self.name, "family": self.family})
        self.index = 0
        Users.total_users += 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < Users.total_users:
            current_index = self.index
            self.index += 1
            return Users.active_users[current_index]
        raise StopIteration


ali = Users("ali", "alavi", 59)
ahmad = Users("ahmad", "alavi", 40)
hasan = Users("hasan", "alavi", 26)
hossain = Users("hossain", "alavi", 38)

for person in ahmad:
    print(person)
