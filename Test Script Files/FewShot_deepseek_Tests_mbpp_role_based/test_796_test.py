import unittest
from mbpp_796_code import return_sum

class TestReturnSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(return_sum({1: 2, 2: 3, 3: 4}), 9)

    def test_edge_condition(self):
        self.assertEqual(return_sum({}), 0)

    def test_boundary_condition(self):
        self.assertEqual(return_sum({1: 1000000}), 1000000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            return_sum("not a dictionary")
