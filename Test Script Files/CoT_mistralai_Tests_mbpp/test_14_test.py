import unittest
from mbpp_14_code import find_Volume

class TestFindVolume(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(find_Volume(3, 4, 5), 60)
        self.assertEqual(find_Volume(2, 2, 2), 12)
        self.assertEqual(find_Volume(1, 1, 1), 1)

    def test_zero_values(self):
        self.assertEqual(find_Volume(0, 4, 5), 0)
        self.assertEqual(find_Volume(3, 0, 5), 0)
        self.assertEqual(find_Volume(3, 4, 0), 0)

    def test_negative_values(self):
        self.assertEqual(find_Volume(-3, 4, 5), -30)
        self.assertEqual(find_Volume(3, -4, 5), -30)
        self.assertEqual(find_Volume(3, 4, -5), -15)

    def test_mixed_values(self):
        self.assertEqual(find_Volume(3, -4, 5), -30)
        self.assertEqual(find_Volume(-3, 4, 5), -30)
        self.assertEqual(find_Volume(3, 4, -5), -15)
