import unittest
from mbpp_904_code import even_num

class TestEvenNum(unittest.TestCase):

    def test_positive_even_number(self):
        self.assertTrue(even_num(2))

    def test_positive_odd_number(self):
        self.assertFalse(even_num(3))

    def test_negative_even_number(self):
        self.assertTrue(even_num(-4))

    def test_negative_odd_number(self):
        self.assertFalse(even_num(-5))

    def test_zero(self):
        self.assertTrue(even_num(0))

    def test_large_even_number(self):
        self.assertTrue(even_num(1000000000000000000))

    def test_large_odd_number(self):
        self.assertFalse(even_num(1000000000000000001))

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            even_num(3.5)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            even_num("hello")

    def test_boolean_input(self):
        with self.assertRaises(TypeError):
            even_num(True)

    def test_list_input(self):
        with self.assertRaises(TypeError):
            even_num([1, 2, 3])
