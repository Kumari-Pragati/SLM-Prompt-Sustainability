import unittest
from mbpp_424_code import extract_rear

class TestExtractRear(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(extract_rear([]), [])

    def test_single_element_list(self):
        self.assertListEqual(extract_rear([1]), [1])

    def test_multiple_elements_list(self):
        self.assertListEqual(extract_rear([1, 2, 3]), [3, 2, 1])

    def test_list_with_duplicates(self):
        self.assertListEqual(extract_rear([1, 2, 3, 1, 2, 3]), [3, 2, 1, 3, 2, 1])

    def test_list_with_non_list_input(self):
        self.assertRaises(TypeError, extract_rear, (1, 2))

    def test_list_with_empty_sublist(self):
        self.assertListEqual(extract_rear([[], [1], [2, 3]]), [3, 1, 2])
