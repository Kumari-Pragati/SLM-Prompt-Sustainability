import unittest
from mbpp_385_code import get_perrin

class TestGetPerrin(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(get_perrin(0), 3)

    def test_positive_numbers(self):
        self.assertEqual(get_perrin(1), 0)
        self.assertEqual(get_perrin(2), 2)
        self.assertEqual(get_perrin(3), 2)
        self.assertEqual(get_perrin(4), 2)
        self.assertEqual(get_perrin(5), 4)
        self.assertEqual(get_perrin(6), 5)
        self.assertEqual(get_perrin(7), 7)
        self.assertEqual(get_perrin(8), 9)
        self.assertEqual(get_perrin(9), 12)

    def test_negative_numbers(self):
        self.assertEqual(get_perrin(-1), 0)
        self.assertEqual(get_perrin(-2), 3)
        self.assertEqual(get_perrin(-3), 2)
        self.assertEqual(get_perrin(-4), 2)
        self.assertEqual(get_perrin(-5), 2)

    def test_large_numbers(self):
        self.assertEqual(get_perrin(10), 37)
        self.assertEqual(get_perrin(20), 114985)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            get_perrin('a')
        with self.assertRaises(TypeError):
            get_perrin(None)
        with self.assertRaises(TypeError):
            get_perrin([])
