#"Name: Kazuma, Age: 35"
#"Name: Tom, Age: 57"
#"Name: Bob, Age: 77"

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_profile(self):
        print(f"Name: {self.name}, Age: {self.age}")


if __name__ == "__main__":
    users_info = [["Kazuma", 35],
                  ["Tom", 57],
                  ["Bob", 77]]

    kazuma = User("Kazuma", 35)
    kazuma.display_profile()

    tom = User("Tom", 57)
    tom.display_profile()

    bob = User("Bob", 77)
    bob.display_profile()













