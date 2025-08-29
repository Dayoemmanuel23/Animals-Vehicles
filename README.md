Polymorphism Demonstration: Animals and Vehicles 🐢🚗✈️
A Python program that demonstrates object-oriented programming principles, particularly polymorphism, through animals and vehicles that each implement the move() method differently.

Overview
This project showcases how different objects can respond to the same method call in unique ways. Each animal and vehicle class defines its own version of the move() method, demonstrating the power of polymorphism in object-oriented programming.

Features
Polymorphism: Same method name (move()), different implementations across classes

Inheritance: Organized class hierarchy with base classes and specialized subclasses

Interactive Demo: Command-line interface to explore different entities

Visual Appeal: Emoji-enhanced output for better visualization

Class Structure
Base Classes
Animal: Base class for all animals with name, move(), and speak() methods

Vehicle: Base class for all vehicles with brand, move(), and fuel_type() methods

Animal Subclasses
Dog: Moves by running 🐕

Fish: Moves by swimming 🐠

Bird: Moves by flying 🕊️

Snake: Moves by slithering 🐍

Vehicle Subclasses
Car: Moves by driving 🚗

Bicycle: Moves by pedaling 🚴

Airplane: Moves by flying ✈️

Boat: Moves by sailing ⛵

OOP Principles Demonstrated
Polymorphism 🎭
Each class implements the move() method differently while maintaining the same interface:

python
dog.move()  # "Buddy is running 🐕"
fish.move() # "Nemo is swimming 🐠"
car.move()  # "Toyota car is driving 🚗"
Inheritance 📊
All animals inherit from the Animal base class

All vehicles inherit from the Vehicle base class

Each subclass extends functionality with specialized behaviors

Encapsulation 🔒
Each class encapsulates its own:

Data attributes (name, brand)

Behavior implementation (movement style, sounds, fuel types)

Installation and Usage
Ensure you have Python 3.6+ installed

Download or clone the repository

Run the program:

bash
python polymorphism_demo.py
Program Output
The program provides three demonstration modes:

Movement Demonstration: Shows how each entity moves differently

Additional Abilities: Shows unique abilities of each entity type

Interactive Mode: Lets you select specific entities to see their movement

Sample Output:
text
=== MOVEMENT DEMONSTRATION ===
Buddy is running 🐕
Nemo is swimming 🐠
Tweety is flying 🕊️
Slither is slithering 🐍
Toyota car is driving 🚗
Trek bicycle is pedaling 🚴
Boeing airplane is flying ✈️
Yamaha boat is sailing ⛵
Educational Value
This project is perfect for learning:

Polymorphism in object-oriented programming

Class design and inheritance patterns

Method overriding in Python

Creating interactive command-line applications

Extending the Project
You can easily add new entities by:

Creating new subclasses of Animal or Vehicle

Implementing the move() method with unique behavior

Adding any additional specialized methods

Example:

python
class Helicopter(Vehicle):
    def move(self):
        return f"{self.brand} helicopter is hovering 🚁"
    
    def fuel_type(self):
        return f"{self.brand} uses aviation fuel 🛢️"
