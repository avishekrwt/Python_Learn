EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time: int):
    """ Calculate the bake time remaining.
        Function that takes the actual minutes the lasagna has been in the oven as
        an argument and returns how many minutes the lasagna still needs to bake
        based on the `EXPECTED_BAKE_TIME`.
    """
    return (EXPECTED_BAKE_TIME-elapsed_bake_time)
    


#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers):
    """ Calculate the bake time remaining.
        Function that takes the actual minutes the lasagna has been in the oven as
        an argument and returns how many minutes the lasagna still needs to bake
        based on the `EXPECTED_BAKE_TIME`.
    """
    return number_of_layers*PREPARATION_TIME
    


#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """ Calculate the bake time remaining.
        Function that takes the actual minutes the lasagna has been in the oven as
        an argument and returns how many minutes the lasagna still needs to bake
        based on the `EXPECTED_BAKE_TIME`.
    """
    return (preparation_time_in_minutes(number_of_layers)+elapsed_bake_time)
    


