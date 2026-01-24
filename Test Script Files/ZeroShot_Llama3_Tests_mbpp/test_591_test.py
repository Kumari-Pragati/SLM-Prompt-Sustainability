import unittest
from mbpp_591_code import swap_List

class TestSwapList(unittest.TestCase):

    def test_swap_list(self):
        self.assertEqual(swap_List([1, 2, 3, 4, 5]), [5, 2, 3, 4, 1])
        self.assertEqual(swap_List(['a', 'b', 'c', 'd', 'e']), ['e', 'b', 'c', 'd', 'a'])
        self.assertEqual(swap_List([10, 20, 30, 40, 50]), [50, 20, 30, 40, 10])
        self.assertEqual(swap_List(['apple', 'banana', 'cherry', 'date', 'elderberry']), ['elderberry', 'banana', 'cherry', 'date', 'apple'])
        self.assertEqual(swap_List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [10, 2, 3, 4, 5, 6, 7, 8, 9, 1])

    def test_swap_list_empty(self):
        self.assertEqual(swap_List([]), [])

    def test_swap_list_single_element(self):
        self.assertEqual(swap_List([1]), [1])

    def test_swap_list_two_elements(self):
        self.assertEqual(swap_List([1, 2]), [2, 1])
