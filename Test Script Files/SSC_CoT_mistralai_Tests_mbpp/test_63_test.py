import unittest
from mbpp_63_code import range
from 63_code import max_difference

class TestMaxDifference(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(max_difference([1, 2, 3, 4, 5]), 4)
        self.assertEqual(max_difference([-1, 0, 1, 2, 3]), 4)
        self.assertEqual(max_difference([0, 0, 0, 0, 0]), 0)

    def test_edge_input(self):
        self.assertEqual(max_difference([1]), 0)
        self.assertEqual(max_difference([1, 1]), 0)
        self.assertEqual(max_difference([-1, 0]), 1)
        self.assertEqual(max_difference([0, -1]), 1)

    def test_boundary_input(self):
        self.assertEqual(max_difference([-1000, -999, -998, -997, -996]), 1003)
        self.assertEqual(max_difference([999, 1000, 1001, 1002, 1003]), 1003)
        self.assertEqual(max_difference([-1000, -999, -998, -997, -996, -995]), 1005)
        self.assertEqual(max_difference([999, 1000, 1001, 1002, 1003, 1004]), 1004)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_difference(123)
        with self.assertRaises(TypeError):
            max_difference(('a', 'b', 'c'))
