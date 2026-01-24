import unittest
from mbpp_793_code import last

class TestLast(unittest.TestCase):

    def test_last_in_array(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        x = 5
        n = len(arr)
        self.assertEqual(last(arr, x, n), 4)

    def test_last_not_in_array(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        x = 10
        n = len(arr)
        self.assertEqual(last(arr, x, n), -1)

    def test_empty_array(self):
        arr = []
        x = 10
        n = len(arr)
        self.assertEqual(last(arr, x, n), -1)

    def test_single_element_array(self):
        arr = [1]
        x = 1
        n = len(arr)
        self.assertEqual(last(arr, x, n), 0)

    def test_duplicate_elements(self):
        arr = [1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9]
        x = 2
        n = len(arr)
        self.assertEqual(last(arr, x, n), 5)
