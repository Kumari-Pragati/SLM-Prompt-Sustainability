import unittest
from mbpp_810_code import Counter
from 810_code import count_variable

class TestCountVariable(unittest.TestCase):

    def test_normal_case(self):
        self.assertListEqual(count_variable(1, 2, 3, 4), [1, 2, 3, 4])

    def test_edge_cases_positive(self):
        self.assertListEqual(count_variable(0, 1, 2, 3), [0, 1, 2, 3])
        self.assertListEqual(count_variable(1, 0, 2, 3), [1, 0, 2, 3])
        self.assertListEqual(count_variable(1, 2, 0, 3), [1, 2, 0, 3])
        self.assertListEqual(count_variable(1, 2, 3, 0), [1, 2, 3, 0])

    def test_edge_cases_negative(self):
        self.assertListEqual(count_variable(-1, 2, 3, 4), [])
        self.assertListEqual(count_variable(1, -2, 3, 4), [])
        self.assertListEqual(count_variable(1, 2, -3, 4), [])
        self.assertListEqual(count_variable(1, 2, 3, -4), [])

    def test_single_input(self):
        self.assertListEqual(count_variable(1, 2, 1), [1])
        self.assertListEqual(count_variable(1, 1, 1), [1])
        self.assertListEqual(count_variable(1, 1, 1), [1])

    def test_invalid_input(self):
        self.assertRaises(TypeError, count_variable, 'a', 2, 3, 4)
        self.assertRaises(TypeError, count_variable, 1, 'b', 3, 4)
        self.assertRaises(TypeError, count_variable, 1, 2, 'c', 4)
        self.assertRaises(TypeError, count_variable, 1, 2, 3, 'd')
