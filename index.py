class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        pass  # To be overridden by subclasses
    
    def speak(self):
        pass  # To be overridden by subclasses

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def move(self):
        pass  # To be overridden by subclasses
    
    def fuel_type(self):
        pass  # To be overridden by subclasses


# Animal Subclasses
class Dog(Animal):
    def move(self):
        return f"{self.name} is running 🐕"
    
    def speak(self):
        return f"{self.name} says: Woof! 🐶"

class Fish(Animal):
    def move(self):
        return f"{self.name} is swimming 🐠"
    
    def speak(self):
        return f"{self.name} says: Blub blub! 🐟"

class Bird(Animal):
    def move(self):
        return f"{self.name} is flying 🕊️"
    
    def speak(self):
        return f"{self.name} says: Tweet tweet! 🐦"

class Snake(Animal):
    def move(self):
        return f"{self.name} is slithering 🐍"
    
    def speak(self):
        return f"{self.name} says: Hiss! 🐍"


# Vehicle Subclasses
class Car(Vehicle):
    def move(self):
        return f"{self.brand} car is driving 🚗"
    
    def fuel_type(self):
        return f"{self.brand} uses gasoline ⛽"

class Bicycle(Vehicle):
    def move(self):
        return f"{self.brand} bicycle is pedaling 🚴"
    
    def fuel_type(self):
        return f"{self.brand} is human-powered 💪"

class Airplane(Vehicle):
    def move(self):
        return f"{self.brand} airplane is flying ✈️"
    
    def fuel_type(self):
        return f"{self.brand} uses jet fuel 🛢️"

class Boat(Vehicle):
    def move(self):
        return f"{self.brand} boat is sailing ⛵"
    
    def fuel_type(self):
        return f"{self.brand} uses diesel ⚓"


# Demonstration function
def demonstrate_movement(entities):
    """Demonstrate polymorphism by calling move() on different objects"""
    print("=== MOVEMENT DEMONSTRATION ===")
    for entity in entities:
        print(entity.move())
    print()

def demonstrate_abilities(entities):
    """Show other abilities of each entity"""
    print("=== ADDITIONAL ABILITIES ===")
    for entity in entities:
        if isinstance(entity, Animal):
            print(entity.speak())
        elif isinstance(entity, Vehicle):
            print(entity.fuel_type())
    print()


# Create instances of animals and vehicles
def main():
    # Create animals
    animals = [
        Dog("Buddy"),
        Fish("Nemo"),
        Bird("Tweety"),
        Snake("Slither")
    ]
    
    # Create vehicles
    vehicles = [
        Car("Toyota"),
        Bicycle("Trek"),
        Airplane("Boeing"),
        Boat("Yamaha")
    ]
    
    # Combine all entities
    all_entities = animals + vehicles
    
    # Demonstrate polymorphism
    demonstrate_movement(animals)
    demonstrate_movement(vehicles)
    demonstrate_movement(all_entities)
    
    # Show additional abilities
    demonstrate_abilities(animals)
    demonstrate_abilities(vehicles)
    
    # Interactive demonstration
    print("=== INTERACTIVE DEMONSTRATION ===")
    for i, entity in enumerate(all_entities, 1):
        print(f"{i}. {entity.name if hasattr(entity, 'name') else entity.brand}")
    
    while True:
        try:
            choice = input("\nChoose an entity number to see its movement (or 'q' to quit): ")
            if choice.lower() == 'q':
                break
            
            index = int(choice) - 1
            if 0 <= index < len(all_entities):
                print(f"➡️ {all_entities[index].move()}")
            else:
                print("Please enter a valid number!")
        
        except ValueError:
            print("Please enter a number or 'q' to quit!")


if __name__ == "__main__":
    main()