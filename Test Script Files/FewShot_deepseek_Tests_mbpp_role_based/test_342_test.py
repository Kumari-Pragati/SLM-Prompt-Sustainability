import unittest
from mbpp_342_code import find_minimum_range

class TestFindMinimumRange(unittest.TestCase):
    def test_typical_case(self):
        list = [[1, 2, 3], [0, 5, 7], [4, 6]]
        self.assertEqual(find_minimum_range(list), (0, 1))

    def test_edge_case(self):
        list = [[10], [20], [30]]
        self.assertEqual(find_minimum_range(list), (10, 10))

    def test_boundary_case(self):
        list = [[-100, -50], [0, 50], [100, 150]]
        self.assertEqual(find_minimum_range(list), (-100, 100))

    def test_invalid_input(self):
        list = [[1, 2, 3], 'a', [4, 6]]
        with self.assertRaises(TypeError):
            find_minimum_range(list)
