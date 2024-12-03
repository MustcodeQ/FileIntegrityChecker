import unittest
import os
import json
from src.file_scanner import scan_directory, save_hashes

class TestFileScanner(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up test directory and files."""
        cls.test_dir = "test_dir"
        cls.output_file = "test_hashes.json"
        
        os.mkdir(cls.test_dir)
        cls.file_1 = os.path.join(cls.test_dir, "file1.txt")
        cls.file_2 = os.path.join(cls.test_dir, "file2.txt")
        
        with open(cls.file_1, "w") as f:
            f.write("Content of file 1")
        with open(cls.file_2, "w") as f:
            f.write("Content of file 2")

    def test_scan_directory(self):
        """Test scanning a directory and generating file hashes."""
        file_hashes = scan_directory(self.test_dir)
        self.assertIn(self.file_1, file_hashes)
        self.assertIn(self.file_2, file_hashes)

    def test_save_hashes(self):
        """Test saving generated file hashes to a JSON file."""
        file_hashes = scan_directory(self.test_dir)
        save_hashes(file_hashes, self.output_file)
        
        # Verify the file exists and contains the correct data
        with open(self.output_file, "r") as f:
            saved_hashes = json.load(f)
        self.assertIn(self.file_1, saved_hashes)
        self.assertIn(self.file_2, saved_hashes)

    @classmethod
    def tearDownClass(cls):
        """Clean up test files and directories."""
        if os.path.exists(cls.output_file):
            os.remove(cls.output_file)
        if os.path.exists(cls.file_1):
            os.remove(cls.file_1)
        if os.path.exists(cls.file_2):
            os.remove(cls.file_2)
        if os.path.exists(cls.test_dir):
            os.rmdir(cls.test_dir)
