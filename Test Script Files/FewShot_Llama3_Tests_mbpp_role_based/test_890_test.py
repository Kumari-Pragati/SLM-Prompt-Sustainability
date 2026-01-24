import unittest
from mbpp_890_code import find_Extra

class TestFindExtra(unittest.TestCase):
    def test_typical_use_case(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [1, 2, 3, 4, 6]
        n = len(arr1)
        self.assertEqual(find_Extra(arr1, arr2, n), 4)

    def test_edge_case_equal_arrays(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [1, 2, 3, 4, 5]
        n = len(arr1)
        self.assertEqual(find_Extra(arr1, arr2, n), n)

    def test_edge_case_empty_array(self):
        arr1 = []
        arr2 = []
        n = len(arr1)
        self.assertEqual(find_Extra(arr1, arr2, n), n)

    def test_edge_case_single_element_array(self):
        arr1 = [1]
        arr2 = [1]
        n = len(arr1)
        self.assertEqual(find_Extra(arr1, arr2, n), n)

    def test_invalid_input_non_integer_n(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [1, 2, 3, 4, 6]
        n = 'abc'
        with self.assertRaises(TypeError):
            find_Extra(arr1, arr2, n)

    def test_invalid_input_non_list_arr1(self):
        arr1 = 'abc'
        arr2 = [1, 2, 3, 4, 6]
        n = len(arr2)
        with self.assertRaises(TypeError):
            find_Extra(arr1, arr2, n)

    def test_invalid_input_non_list_arr2(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = 'abc'
        n = len(arr1)
        with self.assertRaises(TypeError):
            find_Extra(arr1, arr2, n)
