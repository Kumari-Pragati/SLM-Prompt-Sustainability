import unittest
from mbpp_663_code import find_max_val

class TestFindMaxVal(unittest.TestCase):

    def test_find_max_val(self):
        self.assertEqual(find_max_val(10, 2, 0), 10)
        self.assertEqual(find_max_val(10, 3, 2), 9)
        self.assertEqual(find_max_val(10, 1, 1), -1)
        self.assertEqual(find_max_val(0, 1, 0), 0)
        self.assertEqual(find_max_val(100, 10, 0), 100)
        self.assertEqual(find_max_val(100, 10, 1), 91)
        self.assertEqual(find_max_val(100, 10, 9), 90)
        self.assertEqual(find_max_val(100, 10, 10), -1)
        self.assertEqual(find_max_val(100, 1, 0), 100)
        self.assertEqual(find_max_val(100, 1, 1), -1)
