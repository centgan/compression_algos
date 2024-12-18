import sys
import os


def compress(input_path):
    original_file_size = os.stat(input_path).st_size
    with open(input_path, 'r') as f:
        data = str(f.read())

    # output_string = ''
    output_binary = ''
    last_char = ''
    count_char = 1
    for char in data:
        if char == last_char:
            count_char += 1
        else:
            if last_char != '':
                output_binary += ' ' + format(ord(last_char), 'b') + ' ' + format(ord(chr(count_char)), 'b')
                # output_string += last_char + str(count_char)
            last_char = char
            count_char = 1
    # output_string += last_char + str(count_char)
    output_binary += ' ' + format(ord(last_char), 'b') + ' ' + format(ord(chr(count_char)), 'b')

    # output_binary = ' '.join(format(ord(x), 'b') for x in output_string)
    output_path = input_path.split('.txt')[0]+'_rle_compressed.txt'
    with open(output_path, 'w') as f:
        f.write(output_binary)
    print('Original file size: ' + str(original_file_size), ' bytes')
    print('Compressed file size: ' + str(os.stat(output_path).st_size) + ' bytes')


def decompress(input_path):
    with open(input_path, 'r') as f:
        data = f.read()

    each_byte = data.split()
    og_string = ''
    for byte_index in range(0, len(each_byte)-1, 2):
        char = chr(int(each_byte[byte_index], 2))
        count = int(each_byte[byte_index+1], 2)
        og_string += char * count
    formatted = og_string[2:-1].encode().decode('utf-8')[3:]
    with open('moby_dick_rle_uncompressed.txt', 'w') as f:
        f.write(formatted)

    print('The original data is: ', formatted)


if __name__ == '__main__':
    option = sys.argv[1]
    path = sys.argv[2]

    if option == 'compress':
        compress(path)
    elif option == 'decompress':
        decompress(path)
    else:
        print('Invalid option')

