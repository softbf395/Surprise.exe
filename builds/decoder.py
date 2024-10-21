import os

def decode_zero_width(encoded_file, output_file):
    with open(encoded_file, "r", encoding="utf-8") as f:
        encoded_string = f.read()

    # Remove hint if present
    encoded_string = encoded_string.split("\nHint:")[0]
    
    binary_string = encoded_string.replace('\u200C', '0').replace('\u200D', '1')
    byte_array = bytearray(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))

    with open(output_file, "wb") as f:
        f.write(byte_array)

if __name__ == "__main__":
    decode_zero_width("encoded.exe", "app.exe")
