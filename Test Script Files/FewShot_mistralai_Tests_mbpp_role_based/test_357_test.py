import unittest
from mbpp_357_code import find_max

class TestFindMax(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_max([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 9)

    def test_empty_list(self):
        self.assertEqual(find_max([]), None)

    def test_single_element_list(self):
        self.assertEqual(find_max([[1]]), 1)

    def test_list_with_single_number(self):
        self.assertEqual(find_max([1]), 1)

    def test_list_with_negative_numbers(self):
        self.assertEqual(find_max([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), -9)

    def test_list_with_mixed_types(self):
        self.assertRaises(TypeError, find_max, [[1, 'a', 3], [4, 'b', 5], [7, 'c', 9]])
