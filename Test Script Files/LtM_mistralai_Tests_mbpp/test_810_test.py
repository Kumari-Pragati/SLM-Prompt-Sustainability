import unittest
from mbpp_810_code import Counter
from 810_code import count_variable

class TestCountVariable(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertListEqual(count_variable(1, 2, 3, 4), [1, 2, 3, 4])
        self.assertListEqual(count_variable(2, 2, 2, 2), [2])
        self.assertListEqual(count_variable(3, 3, 3, 3), [3])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(count_variable(0, 0, 0, 0), [])
        self.assertListEqual(count_variable(1, 0, 0, 0), [1])
        self.assertListEqual(count_variable(0, 1, 0, 0), [1])
        self.assertListEqual(count_variable(0, 0, 1, 0), [1])
        self.assertListEqual(count_variable(0, 0, 0, 1), [1])

        self.assertListEqual(count_variable(1000000, 1000000, 1000000, 1000000), [1000000])

    def test_complex_inputs(self):
        self.assertListEqual(count_variable(1, 2, 3, 4), [1, 2, 3, 4])
        self.assertListEqual(count_variable(2, 2, 1, 3), [2, 2, 1, 3])
        self.assertListEqual(count_variable(3, 3, 2, 1), [3, 3, 2, 1])
        self.assertListEqual(count_variable(4, 4, 3, 2), [4, 4, 3, 2])
