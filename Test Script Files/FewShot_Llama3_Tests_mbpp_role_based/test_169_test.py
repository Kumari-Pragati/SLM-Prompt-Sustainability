import unittest
from mbpp_169_code import get_pell

class TestGetPell(unittest.TestCase):
    def test_small_numbers(self):
        self.assertEqual(get_pell(1), 1)
        self.assertEqual(get_pell(2), 2)
        self.assertEqual(get_pell(3), 2)

    def test_positive_numbers(self):
        self.assertEqual(get_pell(4), 3)
        self.assertEqual(get_pell(5), 5)
        self.assertEqual(get_pell(6), 8)
        self.assertEqual(get_pell(7), 13)
        self.assertEqual(get_pell(8), 21)

    def test_large_numbers(self):
        self.assertEqual(get_pell(10), 55)
        self.assertEqual(get_pell(11), 89)
        self.assertEqual(get_pell(12), 144)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_pell('a')
