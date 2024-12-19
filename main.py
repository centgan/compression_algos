import sys
from itertools import islice


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def take(n, iterable):
    return list(islice(iterable, n))


def compress(input_path):
    occurrences = {}
    with open(input_path, 'r') as file:
        data = file.read()

    data = 'AAAbb DDDDDD'

    for char in data:
        if char not in occurrences.keys():
            occurrences[char] = 1
        else:
            occurrences[char] += 1

    node_dict = {}
    tree = None
    while True:
        # first sort occurrences
        occurrences = {k: v for k, v in sorted(occurrences.items(), key=lambda item: item[1])}

        # Take the characters with the lowest 2 occurrences
        lowest = take(2, occurrences)
        print(lowest, occurrences)
        lowest_one = occurrences.pop(lowest[0])
        lowest_two = occurrences.pop(lowest[1])
        total = lowest_one + lowest_two

        if len(occurrences) == 0:
            if lowest[0] in node_dict.keys():
                if lowest[1] in node_dict.keys():
                    tree = Node(total, node_dict[lowest[0]], node_dict[lowest[1]])
                else:
                    tree = Node(total, node_dict[lowest[0]], lowest[1])
            elif lowest[1] in node_dict.keys():
                tree = Node(total, lowest[0], node_dict[lowest[1]])
            else:
                tree = Node(total, lowest[0], lowest[1])
            break

        occurrences[lowest[0] + lowest[1]] = total
        node_dict[lowest[0] + lowest[1]] = Node(total, lowest[0], lowest[1])
        if tree is None:
            tree = Node(total, lowest[0], lowest[1])
            print(tree)
        else:
            if lowest[0] in node_dict.keys():
                if lowest[1] in node_dict.keys():
                    tree = Node(total, node_dict[lowest[0]], node_dict[lowest[1]])
                else:
                    tree = Node(total, node_dict[lowest[0]], lowest[1])
            elif lowest[1] in node_dict.keys():
                tree = Node(total, lowest[0], node_dict[lowest[1]])
            else:
                tree = Node(total, lowest[0], lowest[1])

    print(tree)
    print(tree.left, tree.right)
    print(f"'{tree.left}' : '{tree.right.left}' : '{tree.right.right}'")
    # print(node_dict)


def decompress(input_path):
    pass


if __name__ == '__main__':
    option = sys.argv[1]
    inputs = sys.argv[2]
    if option == 'compress':
        compress(inputs)
    elif option == 'decompress':
        decompress(inputs)
    else:
        print("Invalid option")

