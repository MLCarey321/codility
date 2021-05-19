def solution(H):
    N = len(H)
    tallest = max(H)
    indices = [i for i, x in enumerate(H) if x == tallest]
    print(f"Tallest building, size {tallest}, found at locations {indices}")
    if 0 in indices:
        # only look to the right
        right = max(indices) + 1
        # print(f"\tTallest is first, looking at buildings starting at {right}")
        if right == N:
            # print("\t\tTallest is book-ends")
            return N * tallest
        next_tallest = max(H[right:])
        # print(f"\t\tTallest building to right is size {next_tallest}")
        return (right * tallest) + ((N - right) * next_tallest)
    if N-1 in indices:
        # only look to the left
        left = min(indices)
        # print(f"\tTallest is last, looking at buildings to left of {left}")
        next_tallest = max(H[:left])
        # print(f"\t\tTallest building to left is size {next_tallest}")
        return (left * next_tallest) + ((N - left) * tallest)
    # look on both sides
    left = min(indices)
    best_left = N * tallest
    while left > 0:
        print(f"Calculating shorter fabric on left, up to {left}")
        left_tallest = max(H[:left])
        left_result = (left * left_tallest) + ((N - left) * tallest)
        best_left = min(best_left, left_result)
        left = H.index(left_tallest)
    right = max(indices) + 1
    best_right = N * tallest
    while right < N - 1:
        print(f"Calculating shorter fabric on right, starting at {right}")
        right_tallest = max(H[right:])
        right_result = (right * tallest) + ((N - right) * right_tallest)
        best_right = min(best_right, right_result)
        right = H.index(right_tallest, right) + 1
    return min(best_left, best_right)


with open("palladium2020_test_data.txt") as reader:
    lines = reader.readlines()
    for line in lines:
        args = eval(line)
        print(solution(args))
        # break
