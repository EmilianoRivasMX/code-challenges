if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split(" "))
    scores = list(set(arr))
    scores.sort()
    print(scores)

    # Constraint
    if n in range(2,11):
        runner_up_score = scores[-2]
        print(f"\nrunner_up_score = {runner_up_score}\n")
    else: 
        print("Constraint failed")
