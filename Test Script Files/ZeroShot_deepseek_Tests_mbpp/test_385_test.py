import unittest
from mbpp_385_code import get_perrin

class TestPerrin(unittest.TestCase):

    def test_get_perrin_zero(self):
        self.assertEqual(get_perrin(0), 3)

    def test_get_perrin_one(self):
        self.assertEqual(get_perrin(1), 0)

    def test_get_perrin_two(self):
        self.assertEqual(get_perrin(2), 2)

    def test_get_perrin_three(self):
        self.assertEqual(get_perrin(3), 2)

    def test_get_perrin_four(self):
        self.assertEqual(get_perrin(4), 4)

    def test_get_perrin_five(self):
        self.assertEqual(get_perrin(5), 5)

    def test_get_perrin_six(self):
        self.assertEqual(get_perrin(6), 7)

    def test_get_perrin_seven(self):
        self.assertEqual(get_perrin(7), 10)

    def test_get_perrin_eight(self):
        self.assertEqual(get_perrin(8), 12)

    def test_get_perrin_nine(self):
        self.assertEqual(get_perrin(9), 17)

    def test_get_perrin_ten(self):
        self.assertEqual(get_perrin(10), 22)
