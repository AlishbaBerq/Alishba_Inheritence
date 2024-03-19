import streamlit as st

# Define the parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        pass

# Define a subclass inheriting from Animal
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Define another subclass inheriting from Animal
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Streamlit application code
def main():
    st.title("Animal Sounds")
    
    # Create instances of Dog and Cat
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    
    st.write(f"{dog.name} says: {dog.make_sound()}")
    st.write(f"{cat.name} says: {cat.make_sound()}")

if __name__ == "__main__":
    main()
