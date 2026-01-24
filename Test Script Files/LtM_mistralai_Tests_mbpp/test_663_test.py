import unittest
from mbpp_663_code import find_max_val

class TestFindMaxVal(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_max_val(3, 1, 0), 1)
        self.assertEqual(find_max_val(5, 2, 1), 3)
        self.assertEqual(find_max_val(10, 3, 2), 8)

    def test_edge_cases(self):
        self.assertEqual(find_max_val(0, 1, 0), -1)
        self.assertEqual(find_max_val(1, 1, 0), 0)
        self.assertEqual(find_max_val(1, 2, 1), -1)
        self.assertEqual(find_max_val(1, 1, 2), -1)

    def test_boundary_cases(self):
        self.assertEqual(find_max_val(sys.maxsize, 1, 0), sys.maxsize)
        self.assertEqual(find_max_val(sys.maxsize, 2, 1), sys.maxsize)
