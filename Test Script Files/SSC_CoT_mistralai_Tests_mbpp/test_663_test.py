import unittest
from mbpp_663_code import find_max_val

class TestFindMaxVal(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(find_max_val(10, 2, 0), 10)
        self.assertEqual(find_max_val(10, 3, 0), 9)
        self.assertEqual(find_max_val(10, 4, 0), 6)
        self.assertEqual(find_max_val(10, 5, 0), 5)

    def test_edge_cases(self):
        self.assertEqual(find_max_val(0, 2, 0), -1)
        self.assertEqual(find_max_val(1, 2, 0), -1)
        self.assertEqual(find_max_val(2, 2, 1), 2)
        self.assertEqual(find_max_val(2, 3, 0), -1)
        self.assertEqual(find_max_val(2, 4, 1), 1)

    def test_boundary_cases(self):
        self.assertEqual(find_max_val(1, 2, 0), -1)
        self.assertEqual(find_max_val(2, 2, 1), 2)
        self.assertEqual(find_max_val(3, 2, 0), -1)
        self.assertEqual(find_max_val(4, 3, 1), 3)
        self.assertEqual(find_max_val(5, 4, 0), -1)

    def test_invalid_inputs(self):
        self.assertEqual(find_max_val(-1, 2, 0), -1)
        self.assertEqual(find_max_val(10, -1, 0), -1)
        self.assertEqual(find_max_val(10, 2, -1), -1)
