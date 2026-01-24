import unittest
from mbpp_591_code import swap_List

class TestSwapList(unittest.TestCase):
    def test_swap_list(self):
        self.assertEqual(swap_List([1, 2, 3, 4, 5]), [5, 2, 3, 4, 1])
        self.assertEqual(swap_List(['a', 'b', 'c', 'd', 'e']), ['e', 'b', 'c', 'd', 'a'])
        self.assertEqual(swap_List([10, 20, 30, 40, 50]), [50, 20, 30, 40, 10])
        self.assertEqual(swap_List(['apple', 'banana', 'cherry', 'date', 'elderberry']), ['elderberry', 'banana', 'cherry', 'date', 'apple'])
        self.assertEqual(swap_List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [10, 2, 3, 4, 5, 6, 7, 8, 9, 1])
        self.assertEqual(swap_List(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']), ['j', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'a'])
        self.assertEqual(swap_List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), [15, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1])
        self.assertEqual(swap_List(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o']), ['o', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'a'])
        self.assertEqual(swap_List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), [16, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1])
        self.assertEqual(swap_List(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p']), ['p', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'a'])
        self.assertEqual(swap_List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), [17, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1])
        self.assertEqual(swap_List(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q']), ['q', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'a'])
        self.assertEqual(swap_List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), [18, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16