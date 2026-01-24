import unittest
from mbpp_351_code import first_Element

class TestFirstElement(unittest.TestCase):

    def test_first_element_exists(self):
        arr = [1, 7, 4, 3, 4, 8, 7]
        n = len(arr)
        k = 2
        self.assertNotEqual(first_Element(arr, n, k), -1)

    def test_first_element_not_exists(self):
        arr = [1, 7, 4, 3, 4, 8, 7]
        n = len(arr)
        k = 3
        self.assertEqual(first_Element(arr, n, k), -1)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        k = 1
        self.assertEqual(first_Element(arr, n, k), -1)

    def test_single_element_array(self):
        arr = [1]
        n = len(arr)
        k = 1
        self.assertEqual(first_Element(arr, n, k), 1)

    def test_multiple_elements_array(self):
        arr = [1, 2, 2, 1]
        n = len(arr)
        k = 2
        self.assertEqual(first_Element(arr, n, k), 1)
