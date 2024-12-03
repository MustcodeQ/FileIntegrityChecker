import json
from src.hash_util import get_file_hash

def load_hashes(file_path):
    """Loads stored file hashes from a JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def compare_file_hashes(file_path, stored_hash, hash_algorithm='sha256'):
    """Compares the current file hash with the stored hash."""
    current_hash = get_file_hash(file_path, hash_algorithm)
    return current_hash == stored_hash
