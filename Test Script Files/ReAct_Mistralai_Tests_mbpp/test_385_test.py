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
        self.assertEqual(get_perrin(3), get_perrin(1) + get_perrin(0))

    def test_negative_numbers(self):
        self.assertEqual(get_perrin(-1), None)
        self.assertEqual(get_perrin(-2), None)
        self.assertEqual(get_perrin(-3), None)

    def test_large_numbers(self):
        self.assertEqual(get_perrin(100), get_perrin(98) + get_perrin(97))
        self.assertEqual(get_perrin(1000), get_perrin(999) + get_perrin(998))
