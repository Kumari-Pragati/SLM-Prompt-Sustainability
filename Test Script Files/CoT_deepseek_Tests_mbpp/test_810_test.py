import unittest
from mbpp_810_code import count_variable

class TestCountVariable(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_variable(1, 2, 3, 4), ['p', 1, 'q', 2, 'r', 3, 's', 4])

    def test_zero_values(self):
        self.assertEqual(count_variable(0, 0, 0, 0), ['p', 0, 'q', 0, 'r', 0, 's', 0])

    def test_negative_values(self):
        self.assertEqual(count_variable(-1, -2, -3, -4), ['p', -1, 'q', -2, 'r', -3, 's', -4])

    def test_large_values(self):
        self.assertEqual(count_variable(1000, 2000, 3000, 4000), ['p', 1000, 'q', 2000, 'r', 3000, 's', 4000])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_variable('a', 'b', 'c', 'd')
        with self.assertRaises(TypeError):
            count_variable(1, 2, 3)
        with self.assertRaises(TypeError):
            count_variable(1, 2, 3, 4, 5)
