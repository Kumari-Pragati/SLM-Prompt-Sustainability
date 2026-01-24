import unittest
from mbpp_810_code import Counter
from 810_code import count_variable

class TestCountVariable(unittest.TestCase):

    def test_typical_input(self):
        self.assertListEqual(count_variable(1, 2, 3, 4), [1, 2, 3, 4])
        self.assertListEqual(count_variable(5, 6, 7, 8), [5, 6, 7, 8])

    def test_edge_cases(self):
        self.assertListEqual(count_variable(0, 0, 0, 0), [])
        self.assertListEqual(count_variable(1, 2, 3, 4, 5), [1, 2, 3, 4, 5])

    def test_invalid_input(self):
        self.assertRaises(TypeError, count_variable, 'a', 'b', 'c', 'd')
        self.assertRaises(TypeError, count_variable, 1.0, 2.0, 3.0, 4.0)
