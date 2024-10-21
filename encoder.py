import sys

def encode_to_zero_width(input_file, output_file):
    with open(input_file, "rb") as f:
        binary_data = f.read()

    binary_string = ''.join(f'{byte:08b}' for byte in binary_data)
    encoded_string = binary_string.replace('0', '\u200C').replace('1', '\u200D')

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(encoded_string)

if __name__ == "__main__":
    encode_to_zero_width(sys.argv[1], sys.argv[2])
