def solution(P, T, A, B):
    pt = list(zip(P, T))
    gifts = {i: pt[i] for i in range(len(pt)) if pt[i][0] != pt[i][1]}
    # print(gifts)
    pairs = list(zip(A, B))

    class Network:
        def __init__(self, size):
            self.groups = [set([i]) for i in range(size)]
            # print(self)

        def __repr__(self):
            retval = "Network Representation:\n"
            for group in self.groups:
                retval += f"\t{group}\n"
            return retval

        def get_group(self, member):
            return [g for g in self.groups if member in g][0]

        def add_relationship(self, a, b):
            # print(f"Adding relationship: {a}, {b}")
            groupA = self.get_group(a)
            groupB = self.get_group(b)
            if groupA != groupB:
                groupA.update(groupB)
                self.groups.remove(groupB)

    network = Network(len(pt))
    for pair in pairs:
        network.add_relationship(pair[0], pair[1])
        if len(network.groups) == 1:
            break
    # print(network)
    for group in network.groups:
        bad_toys = [gifts[g][1] for g in gifts.keys() if g in group and gifts[g][0] != gifts[g][1]]
        cd = bad_toys.count(1)
        dc = bad_toys.count(2)
        if cd != dc:
            return False
    return True


with open("d2021_test_data.txt") as reader:
    lines = reader.readlines()
    for line in lines:
        args = eval(line)
        print(solution(args[0], args[1], args[2], args[3]))
        # break
