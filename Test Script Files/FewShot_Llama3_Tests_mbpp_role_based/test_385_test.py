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
        self.assertEqual(get_perrin(3), 2)

    def test_four(self):
        self.assertEqual(get_perrin(4), 3)

    def test_five(self):
        self.assertEqual(get_perrin(5), 2)

    def test_six(self):
        self.assertEqual(get_perrin(6), 5)

    def test_seven(self):
        self.assertEqual(get_perrin(7), 5)

    def test_eight(self):
        self.assertEqual(get_perrin(8), 8)

    def test_nine(self):
        self.assertEqual(get_perrin(9), 7)

    def test_ten(self):
        self.assertEqual(get_perrin(10), 12)
