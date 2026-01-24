import unittest
from mbpp_169_code import get_pell

class TestGetPell(unittest.TestCase):

    def test_small_numbers(self):
        self.assertEqual(get_pell(1), 1)
        self.assertEqual(get_pell(2), 2)
        self.assertEqual(get_pell(3), 2)

    def test_pell_numbers(self):
        self.assertEqual(get_pell(4), 3)
        self.assertEqual(get_pell(5), 5)
        self.assertEqual(get_pell(6), 8)
        self.assertEqual(get_pell(7), 13)
        self.assertEqual(get_pell(8), 21)
        self.assertEqual(get_pell(9), 34)
        self.assertEqual(get_pell(10), 55)

    def test_large_numbers(self):
        self.assertEqual(get_pell(11), 89)
        self.assertEqual(get_pell(12), 144)
        self.assertEqual(get_pell(13), 233)
        self.assertEqual(get_pell(14), 377)
        self.assertEqual(get_pell(15), 610)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_pell('a')
