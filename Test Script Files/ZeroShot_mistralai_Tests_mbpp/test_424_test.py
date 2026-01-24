import unittest
from mbpp_424_code import extract_rear

class TestExtractRear(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(extract_rear([]), [])

    def test_single_element_list(self):
        self.assertListEqual(extract_rear([[1]]), [1])

    def test_multiple_elements_list(self):
        self.assertListEqual(extract_rear([[1, 2], [3, 4], [5, 6]]), [2, 4, 6])

    def test_empty_sublist(self):
        self.assertListEqual(extract_rear([[], [1]]), [])

    def test_mixed_sublists(self):
        self.assertListEqual(extract_rear([[], [1], [2, 3], [], [4, 5, 6]]), [3, 4, 5, 6])
