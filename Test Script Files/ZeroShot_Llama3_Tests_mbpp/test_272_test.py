import unittest
from mbpp_272_code import rear_extract

class TestRearExtract(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(rear_extract([]), [])

    def test_single_element_list(self):
        self.assertEqual(rear_extract([[1]]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(rear_extract([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [3, 6, 9])

    def test_list_with_negative_numbers(self):
        self.assertEqual(rear_extract([[-1, -2, -3], [4, 5, 6], [7, 8, 9]]), [-3, 6, 9])

    def test_list_with_mixed_types(self):
        self.assertEqual(rear_extract([['a', 'b', 'c'], [4, 5, 6], [7, 8, 9]]), ['c', 6, 9])
