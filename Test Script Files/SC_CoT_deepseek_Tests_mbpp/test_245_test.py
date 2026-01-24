import unittest

from mbpp_245_code import max_sum

class TestMaxSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sum([1, 2, 3, 4], 4), 8)

    def test_edge_case(self):
        self.assertEqual(max_sum([10, 20, 30, 40], 4), 100)

    def test_corner_case(self):
        self.assertEqual(max_sum([5, 5, 5, 5], 4), 15)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_sum("1, 2, 3, 4", 4)
