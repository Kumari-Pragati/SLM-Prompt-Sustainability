import unittest
from mbpp_357_code import find_max

class TestFindMax(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(find_max([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 9)

    def test_edge_boundary_conditions(self):
        self.assertEqual(find_max([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 0)
        self.assertEqual(find_max([[1], [2], [3]]), 3)
        self.assertEqual(find_max([[100], [200], [300]]), 300)
        self.assertEqual(find_max([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), 0)

    def test_complex_cases(self):
        self.assertEqual(find_max([[10, 20, 30], [40, 50, 60], [70, 80, 90]]), 90)
        self.assertEqual(find_max([[1, 2, 3], [4, 5, 6], [7, 8, 90]]), 90)
        self.assertEqual(find_max([[1, 2, 3], [4, 5, 60], [7, 8, 9]]), 60)
        self.assertEqual(find_max([[1, 2, 3], [4, 5, 6], [70, 8, 9]]), 70)
