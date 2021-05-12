from collections import Counter
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, L, R):
    A.sort()
    lset = set([l for l in A if l < L])
    #for l in lset:
    #    A.remove(l)
    A = list(Counter(A) - Counter(lset))
    A.sort(reverse=True)
    rset = set([r for r in A if r > R])
    solution = len(lset) + len(rset)
    return solution


with open("cmtfc2021_test_data.txt") as reader:
    lines = reader.readlines()
    for line in lines:
        args = eval(line)
        print(solution(args[0], args[1], args[2]))
        #break
