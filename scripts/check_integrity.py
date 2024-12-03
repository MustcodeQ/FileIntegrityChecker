import sys
from src.file_checker import load_hashes, compare_file_hashes

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_integrity.py <hashes_file>")
        sys.exit(1)

    hashes_file = sys.argv[1]
    stored_hashes = load_hashes(hashes_file)
    for file_path, stored_hash in stored_hashes.items():
        result = compare_file_hashes(file_path, stored_hash)
        if not result:
            print(f"File modified: {file_path}")
        else:
            print(f"File intact: {file_path}")
