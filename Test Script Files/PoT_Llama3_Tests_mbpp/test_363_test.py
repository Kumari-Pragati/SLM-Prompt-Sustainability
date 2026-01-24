import unittest
from mbpp_363_code import add_K_element

class TestAddKElement(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(add_K_element([(1, 2), (3, 4)], 5), [(6, 7), (8, 9)])

    def test_edge_case(self):
        self.assertEqual(add_K_element([(1, 2)], 0), [(1, 2)])

    def test_edge_case2(self):
        self.assertEqual(add_K_element([(1, 2)], -1), [(-1, 1), (0, 3)])

    def test_edge_case3(self):
        self.assertEqual(add_K_element([(-1, 1), (0, 3)], 0), [(-1, 1), (0, 3)])

    def test_edge_case4(self):
        self.assertEqual(add_K_element([(-1, 1), (0, 3)], 1), [(-1 + 1, 1 + 1), (0 + 1, 3 + 1)])

    def test_edge_case5(self):
        self.assertEqual(add_K_element([(-1, 1), (0, 3)], 10), [9, 13])

    def test_edge_case6(self):
        self.assertEqual(add_K_element([], 5), [])

    def test_edge_case7(self):
        self.assertEqual(add_K_element([(1, 2)], 5), [(6, 7)])

    def test_edge_case8(self):
        self.assertEqual(add_K_element([(1, 2), (3, 4)], 5), [(6, 7), (8, 9)])
