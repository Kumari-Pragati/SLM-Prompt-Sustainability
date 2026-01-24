import unittest
from mbpp_357_code import find_max

class TestFindMax(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(find_max([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 9)
        self.assertEqual(find_max([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), -9)
        self.assertEqual(find_max([[1000000000], [2000000000], [3000000000]]), 3000000000)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_max([[]]), 0)
        self.assertEqual(find_max([[0]]), 0)
        self.assertEqual(find_max([[0, 0]]), 0)
        self.assertEqual(find_max([[1, 0]]), 1)
        self.assertEqual(find_max([[0, 1]]), 1)
        self.assertEqual(find_max([[0, 0, 0]]), 0)
        self.assertEqual(find_max([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]), 12)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, find_max, [1, 2, 3, "a"])
        self.assertRaises(TypeError, find_max, [1, [2, 3], 4])
        self.assertRaises(TypeError, find_max, [1, [2, 3], [4, "a"]])
