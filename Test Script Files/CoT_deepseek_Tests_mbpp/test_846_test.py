import unittest
from mbpp_846_code import find_platform

class TestFindPlatform(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_platform([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000], 6), 3)

    def test_single_train(self):
        self.assertEqual(find_platform([900], [1000], 1), 1)

    def test_no_trains(self):
        self.assertEqual(find_platform([], [], 0), 0)

    def test_edge_case(self):
        self.assertEqual(find_platform([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000], 6), 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_platform("900, 940, 950, 1100, 1500, 1800", [910, 1200, 1120, 1130, 1900, 2000], 6)
