import unittest
from mbpp_22_code import find_first_duplicate

class TestFindFirstDuplicate(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 2, 4, 2]), 2)
        self.assertEqual(find_first_duplicate([1, 1, 1, 2, 3, 4]), 1)
        self.assertEqual(find_first_duplicate([1, 1, 2, 2, 3, 4]), 2)

    def test_edge_cases(self):
        self.assertEqual(find_first_duplicate([]), -1)
        self.assertEqual(find_first_duplicate([1]), -1)
        self.assertEqual(find_first_duplicate([1, 1]), -1)
        self.assertEqual(find_first_duplicate([1, 1, 1]), -1)
        self.assertEqual(find_first_duplicate([1, 1, 1, 1]), -1)
        self.assertEqual(find_first_duplicate([1, 1, 1, 1, 1]), -1)

    def test_boundary_conditions(self):
        self.assertEqual(find_first_duplicate([0, 1, 2, 3, 4]), -1)
        self.assertEqual(find_first_duplicate([-1, 0, 1, 2, 3]), -1)
        self.assertEqual(find_first_duplicate([1, 2, 3, 4, 5]), -1)
        self.assertEqual(find_first_duplicate([2147483647, 0, 1, 2, 3]), -1)
