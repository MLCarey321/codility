from itertools import chain
from collections import Counter


def solution(A, B):
    dimensions = [set(d) for d in zip(A, B)]
    sides = Counter(chain.from_iterable(dimensions))
    # print(sides)
    # print(sides.most_common(1))
    return sides.most_common(1)[0][1]


with open("silver2020_test_data.txt") as reader:
    lines = reader.readlines()
    for line in lines:
        args = eval(line)
        print(solution(args[0], args[1]))
        # break
