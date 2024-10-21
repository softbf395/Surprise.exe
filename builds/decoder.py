import sys

def decode(encoded_file, output_file):
    # Read the encoded file
    with open(encoded_file, 'r', encoding='utf-8') as file:
        encoded_content = file.read().replace('\n', '')  # Read and remove any newlines

    # Create a binary representation from zero-width characters
    binary_data = ""
    for char in encoded_content:
        if char == '‍':  # Zero Width Joiner (U+200D) represents '1'
            binary_data += '1'
        elif char == '‌':  # Zero Width Non-Joiner (U+200C) represents '0'
            binary_data += '0'

    # Convert binary string to bytes
    byte_array = bytearray()
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if len(byte) < 8:  # Pad with zeros if less than 8 bits
            byte = byte.ljust(8, '0')
        byte_array.append(int(byte, 2))

    # Write the bytes to the output file
    with open(output_file, 'wb') as file:
        file.write(byte_array)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python decoder.py <encoded_file> <output_file>")
        sys.exit(1)

    encoded_file = sys.argv[1]
    output_file = sys.argv[2]
    decode(encoded_file, output_file)
    print(f"Decoded file saved as: {output_file}")
