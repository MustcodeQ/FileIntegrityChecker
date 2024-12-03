import sys
from src.file_scanner import scan_directory, save_hashes

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scan_directory.py <directory_path> <output_file>")
        sys.exit(1)

    directory = sys.argv[1]
    output_file = sys.argv[2]
    file_hashes = scan_directory(directory)
    save_hashes(file_hashes, output_file)
    print(f"File hashes saved to {output_file}")
