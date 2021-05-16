class Tree:
    def __init__(self, left, right, start, length):
        self.left = left
        self.right = right
        self.start = start
        self.length = length
        self.children = []

    def __repr__(self):
        return f"Node from {self.left} to {self.right} with {self.length} layers starting at {self.start} with children {self.children}"

    def addlayer(self, left, right, layer):
        # print(f"Self: {self.left}-{self.right}, {self.start} with {self.length} layers")
        # print(f"\tAdding layer {layer} from {left} to {right}")
        if self.length < 0:
            # print("Invalid node -- aborting")
            return
        if self.start < 0:
            # print("Processing Children")
            for child in [c for c in self.children if left <= c.right and right >= c.left]:
                child.addlayer(left, right, layer)
            return
        left = max(left, self.left)
        right = min(right, self.right)
        if self.left == left and self.right == right:
            if layer == self.length + 1:
                # print("Adding Layer")
                self.length = layer
            else:
                # print("Invalid Layer -- Invalidating Node")
                self.length = -1
            return
        if self.left <= left and self.right >= right:
            # split, set self.start to -1, call addLayer on children
            if self.left < left:
                # print("Creating child to left of layer range")
                self.children.append(Tree(self.left, left-1, self.start, self.length))
            # print("Creating child with layer's range")
            self.children.append(Tree(left, right, self.start, self.length))
            self.children[-1].addlayer(left, right, layer)
            if right < self.right:
                # print("Creating child to right of layer range")
                self.children.append(Tree(right+1, self.right, self.start, self.length))
            self.start = -1
            return

    def cakecountwithlayer(self, layers):
        if self.length < 0:
            # print("Invalid Node Found")
            return 0
        if self.start < 0:
            # print("Parent Node Found")
            return sum([c.cakecountwithlayer(layers) for c in self.children])
        if self.length == layers:
            # print("Terminal Node found with correct layer count!")
            # print(f"Returning {(self.right + 1) - self.left} for cakes {self.left} through {self.right}")
            return (self.right + 1) - self.left
        # print("Terminal Node found with incorrect layer count")
        return 0


def solution(N, K, A, B, C):
    if set(C) != set(range(1, K+1)):
        return 0
    cakes = Tree(left=1, right=N, start=0, length=0)
    for a, b, c in zip(A, B, C):
        cakes.addlayer(a, b, c)
    # print(cakes)
    return cakes.cakecountwithlayer(K)


def solution_one(N, K, A, B, C):
    if set(C) != set(range(1, K+1)):
        return 0
    cakes = {i: 0 for i in range(1, N+1)}
    for i in range(len(A)):
        layer = C[i]
        for cake in list(set(range(A[i], B[i]+1)) & set(cakes.keys())):
            if cakes[cake] != layer-1:
                del(cakes[cake])
            else:
                cakes[cake] = layer
    # print(cakes)
    return len([cake for cake in cakes.values() if cake == K])


def solution_two(N, K, A, B, C):
    if set(C) != set(range(1, K+1)):
        return 0
    # do something clever
    ranges = list(map(lambda a, b, c: (a-1, b, str(c)), A, B, C))
    # print(ranges)
    perfect = "".join([f'{i}' for i in range(1, K+1)])
    # print(perfect)
    layers = []
    for r in ranges:
        layer = [""] * (r[0])
        layer.extend([r[2]] * (r[1]-r[0]))
        layer.extend([""] * (N-r[1]))
        layers.append(layer)
    # print(layers)
    cakes = list(zip(*layers))
    count = len([perfect for cake in cakes if "".join(cake) == perfect])
    # print(cakes)
    return count


with open("gco2021_test_data.txt") as reader:
    lines = reader.readlines()
    for line in lines:
        args = eval(line)
        print(solution(args[0], args[1], args[2], args[3], args[4]))
        # break
