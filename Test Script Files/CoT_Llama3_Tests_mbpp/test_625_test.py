import unittest
from mbpp_625_code import swap_List

class TestSwapList(unittest.TestCase):
    def test_swap_list(self):
        self.assertEqual(swap_List([1, 2, 3, 4, 5]), [5, 2, 3, 4, 1])
        self.assertEqual(swap_List(['a', 'b', 'c', 'd', 'e']), ['e', 'b', 'c', 'd', 'a'])
        self.assertEqual(swap_List([10, 20, 30, 40, 50]), [50, 20, 30, 40, 10])
        self.assertEqual(swap_List(['hello', 'world', 'python', 'unittest']), ['unittest', 'world', 'python', 'hello', 'hello'])
        self.assertEqual(swap_List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [10, 2, 3, 4, 5, 6, 7, 8, 9, 1])

    def test_empty_list(self):
        self.assertEqual(swap_List([]), [])

    def test_single_element_list(self):
        self.assertEqual(swap_List([1]), [1])

    def test_list_with_duplicates(self):
        self.assertEqual(swap_List([1, 2, 2, 3, 4, 4, 5, 5]), [5, 2, 2, 4, 4, 3, 1, 5])
