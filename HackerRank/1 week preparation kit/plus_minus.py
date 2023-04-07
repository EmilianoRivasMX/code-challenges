#!/bin/python3

""" Plus minus

Given an array of integers, calculate the ratios of its elements that are positive, 
negative, and zero. Print the decimal value of each fraction on a new line with  
places after the decimal.
"""


def plusMinus(arr, n):
    positives = negatives = zeros = 0

    for number in arr:
        if number > 0:
            positives += 1
        elif number < 0:
            negatives += 1
        else:
            zeros =+ 1

    print(f"Positives: {positives}\nNegatives: {negatives}\nZeros: {zeros}")

    positives_ratio = round(positives / n, 6)
    negatives_ratio = round(negatives / n, 6)
    zeros_ratio = round(zeros / n, 6)

    print(positives_ratio)
    print(negatives_ratio)
    print(zeros_ratio)


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)
