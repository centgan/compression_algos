import sys
from itertools import islice
import os


def take(n, iterable):
    return list(islice(iterable, n))


def print_nested_list(nested_list, parent_index="", outputting=None):
    if outputting is None:
        outputting = {}

    for index, element in enumerate(nested_list):
        current_index = parent_index + str(index)
        if isinstance(element, list):
            print_nested_list(element, current_index, outputting)
        else:
            outputting[element] = current_index
    return outputting


def compress(input_path):
    original_file_size = os.stat(input_path).st_size
    occurrences = {}
    with open(input_path, 'r') as file:
        data = file.read()
    if len(data) == 0:
        return

    for char in data:
        if char not in occurrences.keys():
            occurrences[char] = 1
        else:
            occurrences[char] += 1

    if len(occurrences) == 1:
        final_dict = str(data[0]) + '0 0000\n'
        encode = '0'*occurrences[data[0]]
        with open('moby_dick_huff_compressed.txt', 'w') as f:
            f.write(final_dict+encode)
        return

    node_dict = {}
    tree = None
    while True:
        # first sort occurrences
        occurrences = {k: v for k, v in sorted(occurrences.items(), key=lambda item: item[1])}

        # Take the characters with the lowest 2 occurrences
        lowest = take(2, occurrences)
        lowest_one = occurrences.pop(lowest[0])
        lowest_two = occurrences.pop(lowest[1])
        total = lowest_one + lowest_two

        if not occurrences:
            if lowest[0] in node_dict and lowest[1] in node_dict:
                tree = [node_dict[lowest[0]], node_dict[lowest[1]]]
            elif lowest[0] in node_dict:
                tree = [tree, lowest[1]]
            elif lowest[1] in node_dict:
                tree = [lowest[0], tree]
            break

        occurrences[lowest[0] + lowest[1]] = total

        if lowest[0] in node_dict and lowest[1] in node_dict:
            node_dict[lowest[0] + lowest[1]] = [node_dict[lowest[0]], node_dict[lowest[1]]]
        elif lowest[0] in node_dict:
            node_dict[lowest[0] + lowest[1]] = [node_dict[lowest[0]], lowest[1]]
        elif lowest[1] in node_dict:
            node_dict[lowest[0] + lowest[1]] = [lowest[0], node_dict[lowest[1]]]
        else:
            node_dict[lowest[0] + lowest[1]] = [lowest[0], lowest[1]]

        if tree is None:
            tree = [lowest[0], lowest[1]]
        else:
            if lowest[0] in node_dict and lowest[1] in node_dict:
                tree = [node_dict[lowest[0]], node_dict[lowest[1]]]
            elif lowest[0] in node_dict:
                tree = [tree, lowest[1]]
            elif lowest[1] in node_dict:
                tree = [lowest[0], tree]

    # # create dict
    outputting = print_nested_list(tree)
    final_dict = ''
    for i in outputting:
        final_dict += i + outputting[i] + ' '
    final_dict += '0000\n'

    encode = ''
    for i in data:
        encode += outputting[i]
    with open('moby_dick_huff_compressed.txt', 'w') as f:
        f.write(final_dict + encode)

    print('Original file size: ' + str(original_file_size), ' bytes')
    print('Compressed file size: ' + str(os.stat('moby_dick_huff_compressed.txt').st_size) + ' bytes')


def decompress(input_path):
    og_string = ''
    dict_encode = {}

    with open(input_path, 'r') as file:
        data = file.read()
    splitting = data.split(' 0000')
    encoding = splitting[0]
    compressed = splitting[1]

    encoding = encoding.split(' ')
    i = 0
    while i < len(encoding):
        if encoding[i] == '':
            dict_encode[encoding[i+1]] = ' '
            i += 2
            continue
        dict_encode[encoding[i][1:]] = encoding[i][0]
        i += 1

    compressed = compressed.replace('\n', '')
    hold = ''
    for j in compressed:
        hold += j
        if hold in dict_encode:
            og_string += dict_encode[hold]
            hold = ''
    with open('moby_dick_huff_decompressed.txt', 'w') as f:
        f.write(og_string)


if __name__ == '__main__':
    option = sys.argv[1]

    if option == 'compress':
        compress('moby_dick.txt')
    elif option == 'decompress':
        decompress('moby_dick_huff_compressed.txt')
    else:
        print("Invalid option")

