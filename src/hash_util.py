import hashlib

def get_file_hash(file_path, hash_algorithm='sha256'):
    """Generates a hash for a given file using the specified algorithm."""
    hash_func = hashlib.new(hash_algorithm)
    try:
        with open(file_path, 'rb') as file:
            while chunk := file.read(8192):
                hash_func.update(chunk)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return None
    return hash_func.hexdigest()
