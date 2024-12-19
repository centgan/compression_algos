import os
import sys


def compress(input_path):
    original_file_size = os.stat(input_path).st_size
    with open(input_path, 'r') as f:
        data = f.read()

    print('Original file size: ' + str(original_file_size), ' bytes')
    # print('Compressed file size: ' + str(os.stat(output_path).st_size) + ' bytes')


def decompress(input_path):
    pass


if __name__ == '__main__':
    option = sys.argv[1]
    path = sys.argv[2]

    if option == 'compress':
        compress(path)
    elif option == 'decompress':
        decompress('moby_dick_lzw_compressed.txt')
    else:
        print('Invalid option')