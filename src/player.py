# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    """docstring for Player."""

    def __init__(self, curr_location, inventory=[]):
        self.curr_location = curr_location
        self.inventory = inventory

    def check_inv(self):
        if self.inventory == []:
            print('Player inventory is empty!')
        else:
            print(f'Inventory: {self.inventory}')

    def take_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)
