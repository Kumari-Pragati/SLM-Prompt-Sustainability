import unittest
from mbpp_663_code import find_max_val

class TestFindMaxVal(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_max_val(10, 1, 0), 10)
        self.assertEqual(find_max_val(20, 5, 0), 20)

    def test_boundary_conditions(self):
        self.assertEqual(find_max_val(0, 1, 0), -1)
        self.assertEqual(find_max_val(1, 2, 1), -1)

    def test_edge_conditions(self):
        self.assertEqual(find_max_val(10, 1, 1), -1)
        self.assertEqual(find_max_val(10, 1, 0), 10)
        self.assertEqual(find_max_val(10, 2, 0), 10)
        self.assertEqual(find_max_val(10, 11, 0), -1)

    def test_complex_cases(self):
        self.assertEqual(find_max_val(100, 10, 5), 95)
        self.assertEqual(find_max_val(100, 10, 0), 100)
        self.assertEqual(find_max_val(100, 10, 9), 90)
