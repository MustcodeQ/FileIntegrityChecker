import os
from src.hash_util import get_file_hash

def scan_directory(directory, hash_algorithm='sha256'):
    """Scans a directory and generates hashes for all files."""
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hashes[file_path] = get_file_hash(file_path, hash_algorithm)
    return file_hashes

def save_hashes(file_hashes, output_file):
    """Saves the generated file hashes to a JSON file."""
    import json
    with open(output_file, 'w') as f:
        json.dump(file_hashes, f, indent=4)
