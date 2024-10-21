import sys

def add_hint_to_exe(encoded_file):
    hint = "\nHint: It's behind many folders.\n"
    
    with open(encoded_file, "a", encoding="utf-8") as f:
        f.write(hint)

if __name__ == "__main__":
    add_hint_to_exe(sys.argv[1])
