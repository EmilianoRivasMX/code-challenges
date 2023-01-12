EXPECTED_BAKE_TIME = 40
PREPARATON_TIME    = 2 

def bake_time_remaining(elapsed_bake_time):
    """
    Return the remaining baking time

    This function takes the minutes the lasagna has been in the oven and calculates how many minutes
    it still needs to bake.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """
    Return prepatation time

    This function takes the number of layers of the lasagna and calculates the needed time to 
    prepare the lasagna.
    """

    return PREPARATON_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time

    This function takes two numbers representing the number of layers and the time alredy spent
    baking and calculates the total elapsed minutes spent cooking the lasagna (including preparation time).
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

