import unittest
from mbpp_14_code import find_Volume

class TestFindVolume(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Volume(3, 4, 5), 60)

    def test_edge_case_zero(self):
        self.assertEqual(find_Volume(0, 4, 5), 0)
        self.assertEqual(find_Volume(3, 0, 5), 0)
        self.assertEqual(find_Volume(3, 4, 0), 0)

    def test_edge_case_one(self):
        self.assertEqual(find_Volume(1, 4, 5), 6)
        self.assertEqual(find_Volume(3, 1, 5), 6)
        self.assertEqual(find_Volume(3, 4, 1), 6)

    def test_edge_case_negative(self):
        self.assertEqual(find_Volume(-3, 4, 5), 0)
        self.assertEqual(find_Volume(3, -4, 5), 0)
        self.assertEqual(find_Volume(3, 4, -5), 0)
