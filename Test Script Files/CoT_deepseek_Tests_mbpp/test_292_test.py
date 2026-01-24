import unittest
from mbpp_292_code import find

class TestFindFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find(10, 2), 5)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            find(10, 0)

    def test_negative_numbers(self):
        self.assertEqual(find(-10, -2), 5)
        self.assertEqual(find(-10, 2), -5)
        self.assertEqual(find(10, -2), -5)

    def test_large_numbers(self):
        self.assertEqual(find(10**10, 10**9), 10)

    def test_float_numbers(self):
        self.assertEqual(find(10.5, 2.5), 4.2)

    def test_string_inputs(self):
        with self.assertRaises(TypeError):
            find('10', 2)
        with self.assertRaises(TypeError):
            find(10, '2')
        with self.assertRaises(TypeError):
            find('10', '2')
