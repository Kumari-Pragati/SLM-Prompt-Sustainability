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
        self.assertEqual(get_perrin(4), 5)

    def test_negative_numbers(self):
        self.assertEqual(get_perrin(-1), get_perrin(-2) + get_perrin(-3))
