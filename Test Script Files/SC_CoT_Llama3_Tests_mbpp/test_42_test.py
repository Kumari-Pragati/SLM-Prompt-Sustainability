import unittest
from mbpp_42_code import find_Sum

class TestFindSum(unittest.TestCase):
    def test_typical_input(self):
        arr = [1, 2, 3, 2, 4, 5, 6, 6]
        n = 7
        self.assertEqual(find_Sum(arr, n), 6)

    def test_edge_case(self):
        arr = [1, 1, 1]
        n = 3
        self.assertEqual(find_Sum(arr, n), 1)

    def test_empty_array(self):
        arr = []
        n = 0
        self.assertEqual(find_Sum(arr, n), 0)

    def test_single_element_array(self):
        arr = [1]
        n = 1
        self.assertEqual(find_Sum(arr, n), 1)

    def test_no_duplicates(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        self.assertEqual(find_Sum(arr, n), 0)

    def test_invalid_input_type(self):
        arr = "hello"
        n = 10
        with self.assertRaises(TypeError):
            find_Sum(arr, n)

    def test_invalid_input_type2(self):
        arr = [1, 2, 3]
        n = "hello"
        with self.assertRaises(TypeError):
            find_Sum(arr, n)
