# Composition (Strong Has-a): House owns its Rooms
class Room:
    def __init__(self, name: str):
        self.name = name


class House:
    def __init__(self):
        # The House creates and owns these Room objects directly
        self.rooms = [Room("Kitchen"), Room("Bedroom")]


if __name__ == "__main__":
    # 1. Instantiate the parent object (House)
    my_house = House()

    # 2. Iterate through the Rooms created inside it
    for room in my_house.rooms:
        print(f"Room created: {room.name}")

    # If the House object is deleted, self.rooms goes with it
    del my_house
