import unittest
from mbpp_663_code import find_max_val

class TestFindMaxVal(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_max_val(10, 2, 0), 10)
        self.assertEqual(find_max_val(20, 5, 0), 20)
        self.assertEqual(find_max_val(30, 3, 2), 24)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_max_val(0, 1, 0), 0)
        self.assertEqual(find_max_val(1, 2, 1), -1)
        self.assertEqual(find_max_val(sys.maxsize, 1, 0), sys.maxsize)

    def test_invalid_or_exceptional_inputs(self):
        self.assertEqual(find_max_val(-1, 1, 0), -1)
        self.assertEqual(find_max_val(10, 0, 0), -1)
        self.assertEqual(find_max_val(10, 2, 2), -1)
