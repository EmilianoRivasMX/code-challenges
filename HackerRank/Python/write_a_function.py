def is_leap(year):
    leap = False

    # First solution
    # if year%4 == 0:
    #     if year%100 != 0:
    #         leap = True
    #     elif year%400 == 0:
    #         leap = True

    # Second solution
    if (year%4 == 0) and (year%100 != 0 or year%400 == 0):
        leap = True


    return leap

# year = int(input())
for year in range(1800, 2100):
    if is_leap(year) == True:
        print(f"{year}: {is_leap(year)}")