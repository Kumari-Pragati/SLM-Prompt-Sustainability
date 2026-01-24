import unittest
from mbpp_890_code import find_Extra

class TestFindExtra(unittest.TestCase):

    def test_typical_case(self):
        arr1 = [2, 4, 6, 8, 10]
        arr2 = [2, 4, 6, 8, 10]
        n = len(arr1)
        self.assertEqual(find_Extra(arr1, arr2, n), n)

    def test_edge_case(self):
        arr1 = []
        arr2 = []
        n = 0
        self.assertEqual(find_Extra(arr1, arr2, n), n)

    def test_extra_element_in_first_array(self):
        arr1 = [2, 4, 6, 8, 10, 12]
        arr2 = [2, 4, 6, 8, 10]
        n = len(arr2)
        self.assertEqual(find_Extra(arr1, arr2, n), n)

    def test_extra_element_in_second_array(self):
        arr1 = [2, 4, 6, 8, 10]
        arr2 = [2, 4, 6, 8, 10, 12]
        n = len(arr1)
        self.assertEqual(find_Extra(arr1, arr2, n), n)

    def test_invalid_input(self):
        arr1 = [2, 4, 6, 8, 10]
        arr2 = [2, 4, 6, 8, 10]
        n = -1
        with self.assertRaises(IndexError):
            find_Extra(arr1, arr2, n)
