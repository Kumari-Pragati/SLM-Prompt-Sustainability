import unittest
from mbpp_890_code import find_Extra

class TestFindExtra(unittest.TestCase):

    def test_typical_case(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [1, 2, 3, 4, 6]
        n = len(arr1)
        self.assertEqual(find_Extra(arr1, arr2, n), 4)

    def test_edge_case_equal(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [1, 2, 3, 4, 5]
        n = len(arr1)
        self.assertEqual(find_Extra(arr1, arr2, n), n)

    def test_edge_case_empty(self):
        arr1 = []
        arr2 = []
        n = len(arr1)
        self.assertEqual(find_Extra(arr1, arr2, n), n)

    def test_edge_case_single_element(self):
        arr1 = [1]
        arr2 = [2]
        n = len(arr1)
        self.assertEqual(find_Extra(arr1, arr2, n), 0)

    def test_edge_case_single_element_equal(self):
        arr1 = [1]
        arr2 = [1]
        n = len(arr1)
        self.assertEqual(find_Extra(arr1, arr2, n), n)

    def test_edge_case_single_element_empty(self):
        arr1 = [1]
        arr2 = []
        n = len(arr1)
        self.assertEqual(find_Extra(arr1, arr2, n), 0)
