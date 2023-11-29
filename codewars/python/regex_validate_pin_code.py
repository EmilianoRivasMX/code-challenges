"""
    ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
    If the function is passed a valid PIN string, return true, else return false.
"""
import re

# Sol 1: Without regex expression
# def validate_pin(pin: str):
    # return True if (len(pin) == (4 or 6)) and (pin.isdigit()) else False


def validate_pin(pin: str):
    return bool(re.match(r'^\d{4}(\d{2})?$', pin)) and not bool(re.search(r'\n', pin)) 

print(validate_pin("34522452"))
print(validate_pin("1234"))
print(validate_pin("as"))
print(validate_pin("098765"))
print(validate_pin("234645"))