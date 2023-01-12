import math

if __name__ == "__main__":
    a = int(input())
    b = int(input())

    if (a and b) in range(1, pow(10,10) + 1):
        print("\nConstraint Passed\n")

        print(a+b)
        print(a-b)
        print(a*b)

        print(f"\n{a+b} \n{a-b} \n{a*b}")
    else:
        print("Constraint Failed")