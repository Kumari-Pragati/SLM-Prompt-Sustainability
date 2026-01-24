import unittest
from mbpp_385_code import get_perrin

class TestGetPerrin(unittest.TestCase):

    def test_get_perrin_zero(self):
        self.assertEqual(get_perrin(0), 3)

    def test_get_perrin_one(self):
        self.assertEqual(get_perrin(1), 0)

    def test_get_perrin_two(self):
        self.assertEqual(get_perrin(2), 2)

    def test_get_perrin_three(self):
        self.assertEqual(get_perrin(3), 2)

    def test_get_perrin_four(self):
        self.assertEqual(get_perrin(4), 5)

    def test_get_perrin_five(self):
        self.assertEqual(get_perrin(5), 8)

    def test_get_perrin_six(self):
        self.assertEqual(get_perrin(6), 13)

    def test_get_perrin_seven(self):
        self.assertEqual(get_perrin(7), 22)

    def test_get_perrin_eight(self):
        self.assertEqual(get_perrin(8), 39)

    def test_get_perrin_nine(self):
        self.assertEqual(get_perrin(9), 64)

    def test_get_perrin_ten(self):
        self.assertEqual(get_perrin(10), 105)
