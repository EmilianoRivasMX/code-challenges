import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    # First Solution

    # if n in range(1,101):
    #     print("Constraint passed")
    #     if n % 2 == 0:
    #         if n in range(2,6):
    #             print("Not Weird")
    #         elif n in range(6,21):
    #             print("Weird")
    #         elif n > 20:
    #             print("Not Weird")
    #     else:
    #         print("Weird")
    # else:
    #     print("Constraint failed")

    # Second Solution
    if n in range(1,101):
        print("Weird") if (n % 2 != 0) or (n in range(6, 21)) else print("Not Weird")
        # print("Not Weird") if (n % 2 == 0) and ((n in range(2, 6)) or (n > 20)) else print("Weird")
    
    # Thrid Solution
    # print(["Not Weird", "Weird"][n % 2 == 1 or n>=6 and n <= 20])