import math

def cockroach_speed(speed):
    convertion_factor = 0.036
    return math.floor(speed/convertion_factor)

speed = float(input("Inseta los km/h: "))
print(cockroach_speed(speed))