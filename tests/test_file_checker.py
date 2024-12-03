import unittest
import os
import json
from src.file_checker import load_hashes, compare_file_hashes
from src.hash_util import get_file_hash

class TestFileChecker(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up test files and a stored hashes file."""
        cls.test_file = "test_file.txt"
        cls.stored_hashes_file = "stored_hashes.json"
        
        # Create a test file
        with open(cls.test_file, "w") as f:
            f.write("Test content")
        
        # Generate and save the hash
        file_hash = get_file_hash(cls.test_file)
        stored_hashes = {cls.test_file: file_hash}
        
        with open(cls.stored_hashes_file, "w") as f:
            json.dump(stored_hashes, f)

    def test_load_hashes(self):
        """Test loading stored hashes from a JSON file."""
        loaded_hashes = load_hashes(self.stored_hashes_file)
        self.assertIn(self.test_file, loaded_hashes)

    def test_compare_file_hashes_intact(self):
        """Test comparing an unmodified file's hash."""
        stored_hash = load_hashes(self.stored_hashes_file)[self.test_file]
        result = compare_file_hashes(self.test_file, stored_hash)
        self.assertTrue(result)

    def test_compare_file_hashes_modified(self):
        """Test comparing a modified file's hash."""
        # Modify the file
        with open(self.test_file, "w") as f:
            f.write("Modified content")
        
        stored_hash = load_hashes(self.stored_hashes_file)[self.test_file]
        result = compare_file_hashes(self.test_file, stored_hash)
        self.assertFalse(result)

    @classmethod
    def tearDownClass(cls):
        """Clean up test files."""
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)
        if os.path.exists(cls.stored_hashes_file):
            os.remove(cls.stored_hashes_file)
