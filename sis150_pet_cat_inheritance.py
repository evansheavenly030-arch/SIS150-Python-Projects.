class Pet:
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Animal type: {self.animal_type}")
        print(f"Age: {self.age}")


class Cat(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, "Cat", age)
        self.breed = breed

    def print_info(self):
        super().print_info()
        print(f"Breed: {self.breed}")


def main():
    pet1 = Pet("Dobby", "Dog", 4)
    cat1 = Cat("Kreacher", 3, "Domestic Shorthair")

    print("Pet Information")
    pet1.print_info()

    print("\nCat Information")
    cat1.print_info()


if __name__ == "__main__":
    main()
