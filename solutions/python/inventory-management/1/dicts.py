"""Functions to keep track and alter inventory."""
from collections import Counter

def create_inventory(items : list):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory = {}
    for item in items :
        inventory[item] = inventory.get(item, 0) + 1
    return inventory
        
        
        
        


def add_items(inventory : dict, items: list):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    new_inventory = Counter(inventory) + Counter(items)
    return dict(new_inventory)






def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    update = create_inventory(items)
    for item in inventory : 
        if item in update :
            if inventory.get(item)-update.get(item)>0: # only update the items present in both
                inventory[item] = inventory[item]- update[item]
            else: inventory[item] = 0
    return inventory



def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    inventory.pop(item,0)
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    return [(item, count) for item, count in inventory.items() if count > 0]