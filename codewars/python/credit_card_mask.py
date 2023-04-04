""" Credit Card Mask

Write a function that takes a credit card number, phone number or the answer of the client's 
secret question when he/she is buying something and mask it.

To mask the input you have to change all but the last four characters into '#'

For example:
    maskify("4556364607935616") == "############5616"
    maskify("Skippy") == "##ippy"
"""

def maskify(cc):
    return "#" * (len(cc) - 4) + cc[-4:]
