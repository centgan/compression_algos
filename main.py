import sys
import os


def compress(input_path):
    original_file_size = os.stat(input_path).st_size
    with open(input_path, 'r', encoding='utf-8-sig') as f:
        data = f.read()

    output_list = []
    last_char = ''
    count_char = 1
    byte_data = bytearray()
    for char in data:
        if char == last_char:
            count_char += 1
        else:
            if last_char != '':
                byte_data.extend(int(format(ord(last_char), '016b')[i:i + 8], 2) for i in range(0, 16, 8))
                byte_data.extend(int(format(count_char, '016b')[i:i + 8], 2) for i in range(0, 16, 8))
            last_char = char
            count_char = 1

    byte_data.extend(int(format(ord(last_char), '016b')[i:i + 8], 2) for i in range(0, 16, 8))
    byte_data.extend(int(format(count_char, '016b')[i:i + 8], 2) for i in range(0, 16, 8))

    output_path = input_path.split('.txt')[0]+'_rle_compressed.bin'
    with open(output_path, 'wb') as f:
        f.write(byte_data)
    print('Original file size: ' + str(original_file_size), ' bytes')
    print('Compressed file size: ' + str(os.stat(output_path).st_size) + ' bytes')


def decompress(input_path):
    with open(input_path, 'rb') as f:
        data = f.read()

    recon = ""
    i = 0
    while i < len(data):
        char_bin = ''.join(format(data[i + j], '08b') for j in range(2))
        char_code = int(char_bin, 2)

        count_bin = ''.join(format(data[i + 2 + j], '08b') for j in range(2))
        count = int(count_bin, 2)

        recon += chr(char_code) * count
        i += 4

    with open('moby_dick_rle_uncompressed.txt', 'w') as f:
        f.write(recon)

    print('The original data is: ', recon)


if __name__ == '__main__':
    # text = "Hello"
    # a = [ord(c) for c in text]
    # print(a)
    # binary_data = bytes(a)
    #
    # # Writing the binary data to a file as raw bytes
    # with open('output_binary.bin', 'wb') as file:
    #     file.write(binary_data)
    #
    # print("Binary data written to 'output_binary.bin'")
    option = sys.argv[1]
    path = sys.argv[2]

    if option == 'compress':
        compress(path)
    elif option == 'decompress':
        decompress(path)
    else:
        print('Invalid option')

