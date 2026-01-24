import unittest
from mbpp_14_code import find_Volume

class TestFindVolume(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Volume(10, 5, 3), 150)

    def test_edge_case_zero_length(self):
        self.assertEqual(find_Volume(0, 5, 3), 0)

    def test_edge_case_zero_base(self):
        self.assertEqual(find_Volume(10, 0, 3), 0)

    def test_edge_case_zero_height(self):
        self.assertEqual(find_Volume(10, 5, 0), 0)

    def test_edge_case_zero_all(self):
        self.assertEqual(find_Volume(0, 0, 0), 0)

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            find_Volume(-10, 5, 3)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            find_Volume('a', 5, 3)
