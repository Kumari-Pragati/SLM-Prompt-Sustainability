import unittest
from mbpp_22_code import find_first_duplicate

class TestFindFirstDuplicate(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 2]), 2)
        self.assertEqual(find_first_duplicate([1, 2, 2, 3]), 2)
        self.assertEqual(find_first_duplicate([1, 1, 2, 3]), 1)

    def test_edge_conditions(self):
        self.assertEqual(find_first_duplicate([]), -1)
        self.assertEqual(find_first_duplicate([1]), -1)
        self.assertEqual(find_first_duplicate([1, 2]), -1)
        self.assertEqual(find_first_duplicate([1, 2, 3]), -1)

    def test_boundary_conditions(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 4, 5, 5]), 5)
        self.assertEqual(find_first_duplicate([1, 2, 3, 4, 5, 6, 6]), 6)
        self.assertEqual(find_first_duplicate([1, 2, 3, 4, 5, 6, 7, 7]), 7)

    def test_complex_cases(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]), 10)
        self.assertEqual(find_first_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11]), 11)
        self.assertEqual(find_first_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12]), 12)
