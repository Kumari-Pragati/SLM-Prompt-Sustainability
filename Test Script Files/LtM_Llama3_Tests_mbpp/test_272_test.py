import unittest
from mbpp_272_code import rear_extract

class TestRearExtract(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(rear_extract([[1, 2, 3], [4, 5, 6]]), [3, 6])

    def test_empty_list(self):
        self.assertEqual(rear_extract([]), [])

    def test_single_element_list(self):
        self.assertEqual(rear_extract([[1]]), [1])

    def test_empty_sublist(self):
        self.assertEqual(rear_extract([[], [1, 2, 3]]), [])

    def test_multiple_sublists(self):
        self.assertEqual(rear_extract([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [3, 6, 9])

    def test_sublists_of_differing_lengths(self):
        self.assertEqual(rear_extract([[1, 2, 3], [4, 5], [6, 7, 8, 9]]), [3, 5, 9])
