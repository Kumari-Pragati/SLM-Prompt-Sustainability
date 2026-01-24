import unittest
from mbpp_272_code import rear_extract

class TestRearExtract(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rear_extract([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [3, 6, 9])

    def test_empty_list(self):
        self.assertEqual(rear_extract([]), [])

    def test_single_element_list(self):
        self.assertEqual(rear_extract([[1]]), [1])

    def test_single_sublist(self):
        self.assertEqual(rear_extract([[1, 2, 3]]), [3])

    def test_all_same_elements(self):
        self.assertEqual(rear_extract([[1, 1, 1], [1, 1, 1], [1, 1, 1]]), [1, 1, 1])

    def test_negative_numbers(self):
        self.assertEqual(rear_extract([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), [-3, -6, -9])

    def test_mixed_numbers(self):
        self.assertEqual(rear_extract([[1, -1, 2], [-2, 3, -3], [4, -4, 5]]), [2, -3, 5])
