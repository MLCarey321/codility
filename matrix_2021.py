def solution(A):
    N = len(A)
    limit = max(A)
    target = (limit // 2) + (limit % 2)
    biggest = 0
    tested = []
    while biggest < target <= limit and target not in tested:
        tested.append(target)
        found = False
        streak = 0
        for i in range(N):
            if A[i] >= target:
                streak += 1
            else:
                streak = 0
            if streak == target:
                found = True
                break
        if found:
            biggest = target
            diff = limit - target
            target = (diff // 2) + target + (diff % 2)
        else:
            limit = target
            diff = target - biggest
            target = target - (diff // 2)
    print(f"Tested: {tested}")
    return biggest


with open("matrix2021_test_data.txt") as reader:
    lines = reader.readlines()
    for line in lines:
        args = eval(line)
        print(solution(args))
        # break
