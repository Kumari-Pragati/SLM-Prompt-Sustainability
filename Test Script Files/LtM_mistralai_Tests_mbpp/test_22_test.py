import unittest
from mbpp_22_code import find_first_duplicate

class TestFindFirstDuplicate(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 2]), 2)
        self.assertEqual(find_first_duplicate([1, 1, 2, 3]), 1)
        self.assertEqual(find_first_duplicate([2, 2, 3, 4]), 2)

    def test_edge_and_boundary(self):
        self.assertEqual(find_first_duplicate([]), -1)
        self.assertEqual(find_first_duplicate([1]), -1)
        self.assertEqual(find_first_duplicate([2, 2]), 2)
        self.assertEqual(find_first_duplicate([1000000000, 1000000000]), -1)

    def test_complex(self):
        self.assertEqual(find_first_duplicate([1, 1, 2, 3, 2]), 2)
        self.assertEqual(find_first_duplicate([1, 1, 1, 2, 3]), 1)
        self.assertEqual(find_first_duplicate([2, 2, 2, 3, 4]), 2)
        self.assertEqual(find_first_duplicate([10, 20, 20, 30, 40]), 20)
