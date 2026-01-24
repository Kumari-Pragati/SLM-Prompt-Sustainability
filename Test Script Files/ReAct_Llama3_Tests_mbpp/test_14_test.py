import unittest
from mbpp_14_code import find_Volume

class TestFindVolume(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Volume(10, 5, 3), 150)

    def test_zero_length(self):
        with self.assertRaises(ZeroDivisionError):
            find_Volume(0, 5, 3)

    def test_zero_base(self):
        with self.assertRaises(ZeroDivisionError):
            find_Volume(10, 0, 3)

    def test_zero_height(self):
        with self.assertRaises(ZeroDivisionError):
            find_Volume(10, 5, 0)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            find_Volume(-10, -5, 3)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            find_Volume('a', 5, 3)

    def test_non_numeric_input2(self):
        with self.assertRaises(TypeError):
            find_Volume(10, 'b', 3)

    def test_non_numeric_input3(self):
        with self.assertRaises(TypeError):
            find_Volume(10, 5, 'c')
