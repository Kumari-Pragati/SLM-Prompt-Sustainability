import unittest
from mbpp_385_code import get_perrin

class TestGetPerrin(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(get_perrin(0), 3)

    def test_one(self):
        self.assertEqual(get_perrin(1), 0)

    def test_two(self):
        self.assertEqual(get_perrin(2), 2)

    def test_three(self):
        self.assertEqual(get_perrin(3), 3)

    def test_four(self):
        self.assertEqual(get_perrin(4), 2)

    def test_negative_number(self):
        self.assertRaises(ValueError, get_perrin, -1)

    def test_large_number(self):
        self.assertRaises(ValueError, get_perrin, 100)

    def test_non_integer_input(self):
        self.assertRaises(TypeError, get_perrin, 3.14)
