if __name__ == "__main__":
    n = int(input())

    if n in range(1,151):
        for number in range(n):
            print(number+1, end='')
    else:
        print("Constraint Failed")