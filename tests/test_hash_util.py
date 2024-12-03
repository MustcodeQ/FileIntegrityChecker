import unittest
from src.hash_util import get_file_hash

class TestHashUtil(unittest.TestCase):
    def test_get_file_hash(self):
        with open("test.txt", "w") as f:
            f.write("Test content")
        self.assertEqual(
            get_file_hash("test.txt", "sha256"),
            "b1946ac92492d2347c6235b4d2611184b1600b5b2e97d93f985614b3175d8f6b"
        )
