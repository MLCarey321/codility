def solution(juice, capacity):
    class Cup:
        def __init__(self, j, c):
            self.juice = j
            self.capacity = c
            self.space = c - j

        def __repr__(self):
            return f"Cup(Capacity: {self.capacity}; Juice: {self.juice}; Space: {self.space})"

    cups = {}
    spaces = set()
    N = len(juice)
    for i in range(N):
        cups.update({i: Cup(juice[i], capacity[i])})
        spaces.add(cups[i].space)
    # print(cups)
    # print(f"Size of spaces: {len(spaces)}")
    large_spaces = list(spaces)
    large_spaces.sort(reverse=True)
    # print(large_spaces)
    juice_sorted = sorted(cups.keys(), key=lambda x: cups[x].juice)
    # print(juice_sorted)
    max_count = 0
    for space in large_spaces:
        space_i = sorted([cup for cup in cups.keys() if cups[cup].space == space], key=lambda x: cups[x].juice, reverse=True)[0]
        container = cups[space_i]
        cup_count = 1
        remaining = container.space
        # print(f"Testing cup {space_i} as container")
        exhausted = True
        for juice_i in juice_sorted:
            if juice_i == space_i:
                continue
            # print(f"\tAttempting to add juice from cup {juice_i}")
            juice_cup = cups[juice_i]
            if juice_cup.juice <= remaining:
                # print(f"\t\tAdding juice from cup {juice_i}")
                remaining -= juice_cup.juice
                cup_count += 1
            else:
                # escape condition isn't working; need to find a way to short-circuit for final test case
                if len([cup for cup in cups.keys() if cup in juice_sorted[juice_sorted.index(juice_i)+1:] and
                                                      cups[cup].juice <= container.space]) == 0:
                    exhausted = False
                break
        if cup_count > max_count:
            # print(f"!!Found new max count {cup_count} using cup {container_i}!!")
            max_count = cup_count
        elif cup_count < max_count:
            # print("Point of Diminishing Returns reached -- Aborting")
            break
        if exhausted:
            break
    return max_count


with open("olxg2021_test_data.txt") as reader:
    lines = reader.readlines()
    for line in lines:
        args = eval(line)
        print(solution(args[0], args[1]))
        # break
