import unittest

from mbpp_625_code import swap_List

class TestSwapList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(swap_List([1, 2, 3]), [3, 2, 1])

    def test_single_element_list(self):
        self.assertEqual(swap_List([5]), [5])

    def test_empty_list(self):
        self.assertEqual(swap_List([]), [])

    def test_large_list(self):
        large_list = list(range(1, 1001))
        self.assertEqual(swap_List(large_list), list(range(1000, 0, -1)))

    def test_negative_numbers(self):
        self.assertEqual(swap_List([-1, -2, -3]), [-3, -2, -1])

    def test_zero(self):
        self.assertEqual(swap_List([0]), [0])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            swap_List("not a list")
