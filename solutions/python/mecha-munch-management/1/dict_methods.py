"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for items in items_to_add:
        if items in current_cart.keys():
            current_cart[items] = current_cart[items]+1
        else :
            current_cart[items] = 1

    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    return add_item({},notes)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    new_cart = dict(sorted(cart.items()))
    return new_cart


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    new_dict = {}
    for keys in cart:
        aisle_info = aisle_mapping.get(keys, [None, None])
        new_dict[keys] = [cart[keys],aisle_info[0], aisle_info[1]]

    returning_cart = dict(sorted(new_dict.items(),reverse = True))
    return returning_cart


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for keys in fulfillment_cart:
        store_info = store_inventory.get(keys, None)
        fulfillment_info = fulfillment_cart.get(keys, None)
        variable = store_info[0]-fulfillment_info[0]
        if variable > 0 :
            store_inventory[keys] = [variable,store_info[1],store_info[2]]
        else:
            store_inventory[keys] = ['Out of Stock',store_info[1],store_info[2]]

    return store_inventory
