class Person:
    species = "Homo sapiens"

    def __init__(self, name):
        self.name = name

    @classmethod
    def from_full_name(cls, full_name):
        first_name, last_name = full_name.split()
        return cls(first_name)  # Create a new instance

    @classmethod
    def set_species(cls, new_species):
        cls.species = new_species  # Modify class-level attribute

# Usage
p = Person.from_full_name("John Doe")  # Create an instance using class method
print(p.name)
print(Person.species)

Person.set_species("Homo erectus")  # Modify class-level data
print(Person.species)

