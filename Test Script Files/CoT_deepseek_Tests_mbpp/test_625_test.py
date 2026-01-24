import unittest
from mbpp_625_code import swap_List

class TestSwapList(unittest.TestCase):

    def test_swap_list_with_two_elements(self):
        self.assertEqual(swap_List([1, 2]), [2, 1])

    def test_swap_list_with_three_elements(self):
        self.assertEqual(swap_List([1, 2, 3]), [3, 2, 1])

    def test_swap_list_with_empty_list(self):
        self.assertEqual(swap_List([]), [])

    def test_swap_list_with_single_element(self):
        self.assertEqual(swap_List([1]), [1])

    def test_swap_list_with_same_elements(self):
        self.assertEqual(swap_List([1, 1]), [1, 1])

    def test_swap_list_with_negative_elements(self):
        self.assertEqual(swap_List([-1, -2]), [-2, -1])

    def test_swap_list_with_zero(self):
        self.assertEqual(swap_List([0, 1]), [1, 0])

    def test_swap_list_with_large_numbers(self):
        self.assertEqual(swap_List([1000, 2000]), [2000, 1000])

    def test_swap_list_with_non_integer_elements(self):
        self.assertEqual(swap_List([1.1, 2.2]), [2.2, 1.1])

    def test_swap_list_with_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            swap_List(['a', 'b'])

    def test_swap_list_with_none_elements(self):
        with self.assertRaises(TypeError):
            swap_List([None, None])
