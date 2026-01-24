import unittest
from mbpp_385_code import get_perrin

class TestGetPerrin(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(get_perrin(0), 3)

    def test_one(self):
        self.assertEqual(get_perrin(1), 0)

    def test_two(self):
        self.assertEqual(get_perrin(2), 2)

    def test_negative(self):
        with self.assertRaises(TypeError):
            get_perrin(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            get_perrin('a')

    def test_large(self):
        self.assertEqual(get_perrin(10), get_perrin(8) + get_perrin(7))
