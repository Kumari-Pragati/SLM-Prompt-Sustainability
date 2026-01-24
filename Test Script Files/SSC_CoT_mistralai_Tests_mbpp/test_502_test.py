import unittest
from mbpp_502_code import find

class TestFindFunction(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(find(10, 3), 1)
        self.assertEqual(find(15, 5), 0)

    def test_edge_cases(self):
        self.assertEqual(find(0, 3), 0)
        self.assertEqual(find(1, 1), 0)
        self.assertEqual(find(-1, 3), -1)

    def test_boundary_cases(self):
        self.assertEqual(find(2147483647, 3), 2)
        self.assertEqual(find(-2147483648, 3), -2)
