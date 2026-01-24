import unittest
from mbpp_363_code import add_K_element

class TestAddKElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(add_K_element([(1, 2), (3, 4)], 1), [(2, 3), (4, 5)])
        self.assertListEqual(add_K_element([(0, 0), (1, 1)], 0), [(0, 0), (1, 1)])
        self.assertListEqual(add_K_element([(10, 20), (30, 40)], -5), [(5, -10), (25, -35)])

    def test_edge_case(self):
        self.assertListEqual(add_K_element([], 1), [])
        self.assertListEqual(add_K_element([(0,)], 0), [(0,)])
        self.assertListEqual(add_K_element([(1, 2), (3, 4)], 0), [(1, 2), (3, 4)])

    def test_corner_case(self):
        self.assertListEqual(add_K_element([(sys.maxsize,)], 1), [(sys.maxsize + 1,)])
        self.assertListEqual(add_K_element([(sys.maxsize,)], -1), [(sys.maxsize - 1,)])
