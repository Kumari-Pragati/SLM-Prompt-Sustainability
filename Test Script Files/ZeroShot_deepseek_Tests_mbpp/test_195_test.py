import unittest
from mbpp_195_code import first

class TestFirst(unittest.TestCase):

    def test_first_in_array(self):
        arr = [1, 2, 3, 4, 5]
        x = 3
        n = len(arr)
        self.assertEqual(first(arr, x, n), 2)

    def test_first_not_in_array(self):
        arr = [1, 2, 3, 4, 5]
        x = 6
        n = len(arr)
        self.assertEqual(first(arr, x, n), -1)

    def test_empty_array(self):
        arr = []
        x = 6
        n = len(arr)
        self.assertEqual(first(arr, x, n), -1)

    def test_single_element_array(self):
        arr = [1]
        x = 1
        n = len(arr)
        self.assertEqual(first(arr, x, n), 0)

    def test_duplicate_elements(self):
        arr = [1, 2, 2, 3, 4, 5]
        x = 2
        n = len(arr)
        self.assertEqual(first(arr, x, n), 1)
