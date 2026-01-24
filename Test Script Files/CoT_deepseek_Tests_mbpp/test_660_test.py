import unittest
from mbpp_660_code import find_Points

class TestFindPoints(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Points(1, 2, 3, 4), (-1, -1))

    def test_same_left_right_values(self):
        self.assertEqual(find_Points(1, 1, 1, 1), (-1, -1))

    def test_different_left_right_values(self):
        self.assertEqual(find_Points(1, 2, 3, 4), (1, 4))

    def test_negative_values(self):
        self.assertEqual(find_Points(-1, -2, -3, -4), (-1, -1))

    def test_zero_values(self):
        self.assertEqual(find_Points(0, 2, 0, 4), (0, 4))

    def test_equal_left_values_different_right(self):
        self.assertEqual(find_Points(1, 2, 1, 4), (1, 4))

    def test_equal_right_values_different_left(self):
        self.assertEqual(find_Points(1, 4, 1, 2), (1, 4))

    def test_invalid_input_types(self):
        with self.assertRaises(TypeError):
            find_Points("1", 2, 3, 4)
        with self.assertRaises(TypeError):
            find_Points(1, "2", 3, 4)
        with self.assertRaises(TypeError):
            find_Points(1, 2, "3", 4)
        with self.assertRaises(TypeError):
            find_Points(1, 2, 3, "4")
