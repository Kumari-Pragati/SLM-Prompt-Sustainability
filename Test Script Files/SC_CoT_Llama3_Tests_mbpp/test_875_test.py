import unittest
from mbpp_875_code import min_difference

class TestMinDifference(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(min_difference([(1, 2), (3, 4), (5, 6)]), 1)

    def test_edge_case(self):
        self.assertEqual(min_difference([(1, 1), (2, 2), (3, 3)]), 0)

    def test_edge_case2(self):
        self.assertEqual(min_difference([(1, 2), (2, 1)]), 1)

    def test_edge_case3(self):
        self.assertEqual(min_difference([(1, 2), (2, 2), (3, 3)]), 1)

    def test_edge_case4(self):
        self.assertEqual(min_difference([(1, 2), (2, 3), (3, 4)]), 1)

    def test_edge_case5(self):
        self.assertEqual(min_difference([(1, 1), (2, 2), (3, 3), (4, 4)]), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_difference([1, 2, 3])

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            min_difference([(1, 2), 3, 4])

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            min_difference([1, 2, 3, 4, 5])
