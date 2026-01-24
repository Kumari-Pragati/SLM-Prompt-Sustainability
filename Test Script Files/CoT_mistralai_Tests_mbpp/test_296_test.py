import unittest
from mbpp_296_code import get_Inv_Count

class TestGetInvCount(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(get_Inv_Count([], 0), 0)

    def test_single_element_list(self):
        self.assertEqual(get_Inv_Count([1], 1), 0)

    def test_increasing_list(self):
        self.assertEqual(get_Inv_Count([1, 2, 3, 4], 4), 0)

    def test_decreasing_list(self):
        self.assertEqual(get_Inv_Count([4, 3, 2, 1], 4), 3)

    def test_mixed_list(self):
        self.assertEqual(get_Inv_Count([1, 5, 2, 4, 3], 5), 4)

    def test_duplicates(self):
        self.assertEqual(get_Inv_Count([1, 1, 2, 3], 4), 1)

    def test_negative_numbers(self):
        self.assertEqual(get_Inv_Count([-1, -2, -3], 3), 3)

    def test_zero(self):
        self.assertEqual(get_Inv_Count([0], 1), 0)
        self.assertEqual(get_Inv_Count([0, 1], 2), 1)

    def test_invalid_input_length(self):
        with self.assertRaises(IndexError):
            get_Inv_Count([1, 2, 3], 4)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            get_Inv_Count("abc", 3)
