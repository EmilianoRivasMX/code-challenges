"""
https://www.testdome.com/questions/python/ice-cream-machine/94857

Expected Time: 10 min

Implement the IceCreamMachine's scoops method so that it returns all combinations of one 
ingredient and one topping. If there are no ingredients or toppings, the method should 
return an empty list.

For example:
    IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"]).scoops()
    
    should return: 
        [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']].
"""

from itertools import product

class IceCreamMachine:
    """
    Class to represent an Ice Cream Machine

    Attributes: 
        ingredients (list): List of ingredients
        toppings (list): List of toppings

    Methods:
        scoops(): Returns all combinations of one ingredient and one topping
    """

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    # Solution 1
    def scoops(self):
        """
        This method returns all combinations of one ingredient and one topping

        Returns:
            combinations (list): List of lists with all combinations of one ingredient and one topping
        """
        if self.ingredients and self.toppings:
            # combinations = list(product(self.ingredients, self.toppings)) # Tuplas
            combinations = [list(x) for x in product(self.ingredients, self.toppings)]  # Listas
        else:
            combinations = []

        return combinations

    # Solution 2
    # def scoops(self):
    #     combinations = []

    #     if self.ingredients and self.toppings:
    #         for ingredient in self.ingredients:
    #             for topping in self.toppings:
    #                 combinations.append([ingredient, topping])

    #     return combinations


if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops())
