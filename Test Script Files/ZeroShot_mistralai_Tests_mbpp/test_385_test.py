import unittest
from mbpp_385_code import get_perrin

class TestGetPerrin(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(get_perrin(0), 3)

    def test_one(self):
        self.assertEqual(get_perrin(1), 0)

    def test_two(self):
        self.assertEqual(get_perrin(2), 2)

    def test_negative_numbers(self):
        self.assertEqual(get_perrin(-1), None)
        self.assertEqual(get_perrin(-2), None)
        self.assertEqual(get_perrin(-3), None)

    def test_large_numbers(self):
        self.assertEqual(get_perrin(100), None)
        self.assertEqual(get_perrin(200), None)
        self.assertEqual(get_perrin(300), None)

    def test_invalid_input(self):
        self.assertRaises(TypeError, get_perrin, 'invalid_input')
        self.assertRaises(TypeError, get_perrin, 3.14)
