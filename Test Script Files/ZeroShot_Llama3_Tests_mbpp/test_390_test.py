import unittest
from mbpp_390_code import add_string

class TestAddString(unittest.TestCase):

    def test_add_string(self):
        self.assertEqual(add_string([1, 2, 3], "Hello {}"), ["Hello 1", "Hello 2", "Hello 3"])
        self.assertEqual(add_string([1, 2, 3, 4, 5], "Hello {}"), ["Hello 1", "Hello 2", "Hello 3", "Hello 4", "Hello 5"])
        self.assertEqual(add_string([], "Hello {}"), [])
        self.assertEqual(add_string([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Hello {}"), ["Hello 1", "Hello 2", "Hello 3", "Hello 4", "Hello 5", "Hello 6", "Hello 7", "Hello 8", "Hello 9", "Hello 10"])
        self.assertEqual(add_string([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "Hello {}"), ["Hello 1", "Hello 2", "Hello 3", "Hello 4", "Hello 5", "Hello 6", "Hello 7", "Hello 8", "Hello 9", "Hello 10", "Hello 11", "Hello 12"])
