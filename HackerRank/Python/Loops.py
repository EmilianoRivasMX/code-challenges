import math

if __name__ == "__main__":
    n = int(input())

    if n in range(1, 21):
        print("\nConstraint Passed\n")

        numbers = list(range(n))
        for i in numbers: print(i**2)
    else:
        print("Constraint Failed")
