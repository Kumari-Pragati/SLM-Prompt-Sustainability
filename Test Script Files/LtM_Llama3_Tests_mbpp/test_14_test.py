import unittest
from mbpp_14_code import find_Volume

class TestFindVolume(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(find_Volume(1, 2, 3), 3)

    def test_zero_height(self):
        self.assertEqual(find_Volume(1, 2, 0), 0)

    def test_zero_base(self):
        self.assertEqual(find_Volume(0, 2, 3), 0)

    def test_zero_length(self):
        self.assertEqual(find_Volume(0, 2, 3), 0)

    def test_negative_inputs(self):
        self.assertRaises(ValueError, find_Volume, -1, 2, 3)

    def test_non_numeric_inputs(self):
        with self.assertRaises(TypeError):
            find_Volume('a', 2, 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_Volume(1, 'b', 3)
