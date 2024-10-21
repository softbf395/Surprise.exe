def encode(input_file, output_file):
    # Read the input EXE file in binary mode
    with open(input_file, "rb") as f:
        # Read the binary content and convert each byte to its binary representation
        binary_data = ''.join(f"{byte:08b}" for byte in f.read())

    # Encode binary data to zero-width characters
    encoded_data = ''.join('‍' if bit == '1' else '‌' for bit in binary_data)

    # Write the encoded data to the output file in UTF-8
    with open(output_file, "w", encoding="utf-8") as f1:
        f1.write(encoded_data)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python encoder.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    encode(input_file, output_file)
    print(f"Encoded file saved as: {output_file}")
