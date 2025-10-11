EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time: int):
    """ Calculate the bake time remaining.
        Function that takes the actual minutes the lasagna has been in the oven as
        an argument and returns how many minutes the lasagna still needs to bake
        based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME-elapsed_bake_time
    
def preparation_time_in_minutes(number_of_layers):
    """ Calculate preparation_time_in_minutes.
        Function that takes the actual minutes the lasagna has been in the oven as
        an argument and returns how many minutes the lasagna still needs to bake
        based on the `EXPECTED_BAKE_TIME`.
    """
    return number_of_layers*PREPARATION_TIME
    
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """ Calculate elapsed_time_in_minutes.
        Function that takes the actual minutes the lasagna has been in the oven as
        an argument and returns how many minutes the lasagna still needs to bake
        based on the `EXPECTED_BAKE_TIME`.
    """
    return preparation_time_in_minutes(number_of_layers)+elapsed_bake_time