# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    """docstring for Room."""

    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return f'Location: {self.name} \nDescription: {self.description} \n Items: {self.items}'

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
