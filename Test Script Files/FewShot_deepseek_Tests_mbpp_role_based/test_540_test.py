import unittest
from mbpp_540_code import find_Diff

class TestFindDiff(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Diff([1, 2, 2, 3, 4, 4, 4, 5, 6, 6], 10), 2)

    def test_single_element(self):
        self.assertEqual(find_Diff([1], 1), 0)

    def test_same_elements(self):
        self.assertEqual(find_Diff([1, 1, 1, 1, 1], 5), 0)

    def test_empty_array(self):
        self.assertEqual(find_Diff([], 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(find_Diff([-1, -1, 0, 0, 1, 1], 6), 0)

    def test_large_numbers(self):
        self.assertEqual(find_Diff([1000, 1000, 2000, 2000], 4), 1000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Diff("1, 2, 2, 3, 4, 4, 4, 5, 6, 6", 10)
