import unittest
from mbpp_272_code import rear_extract

class TestRearExtract(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(rear_extract([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [3, 6, 9])

    def test_empty_list(self):
        self.assertEqual(rear_extract([]), [])

    def test_single_element_list(self):
        self.assertEqual(rear_extract([[1]]), [1])

    def test_empty_sublists(self):
        self.assertEqual(rear_extract([[], []]), [])

    def test_negative_numbers(self):
        self.assertEqual(rear_extract([[1, -2, 3], [-4, 5, -6], [7, -8, 9]]), [3, -6, 9])

    def test_mixed_types(self):
        self.assertEqual(rear_extract([[1, 'two', 3], [4, 'five', 6], [7, 'eight', 9]]), [3, 6, 9])

    def test_large_numbers(self):
        self.assertEqual(rear_extract([[1000000, 2000000, 3000000], [4000000, 5000000, 6000000], [7000000, 8000000, 9000000]]), [3000000, 6000000, 9000000])
