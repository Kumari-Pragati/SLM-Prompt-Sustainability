import unittest
from mbpp_357_code import find_max

class TestFindMax(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(find_max([[1], [2], [3]]), 3)
        self.assertEqual(find_max([[-1], [-2], [-3]]), -3)
        self.assertEqual(find_max([[0], [0], [0]]), 0)

    def test_edge_input(self):
        self.assertEqual(find_max([]), None)
        self.assertEqual(find_max([[1000000000000000000]]), 1000000000000000000)
        self.assertEqual(find_max([[-1000000000000000000]]), -1000000000000000000)

    def test_complex_input(self):
        self.assertEqual(find_max([[1, 2], [3, 4], [5, 6]]), 6)
        self.assertEqual(find_max([[-1, -2], [-3, -4], [-5, -6]]), -6)
        self.assertEqual(find_max([[1, -2], [3, -4], [5, -6]]), 5)
        self.assertEqual(find_max([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 9)
        self.assertEqual(find_max([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), -9)
        self.assertEqual(find_max([[1, -2, 3], [4, -5, 6], [7, -8, 9]]), 9)
