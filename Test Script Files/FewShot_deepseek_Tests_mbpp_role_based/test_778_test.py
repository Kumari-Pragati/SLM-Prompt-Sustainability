import unittest
from mbpp_778_code import pack_consecutive_duplicates

class TestPackConsecutiveDuplicates(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1, 2, 2, 3, 3]), [[1, 1], [2, 2], [3, 3]])

    def test_edge_case_single_element(self):
        self.assertEqual(pack_consecutive_duplicates([1]), [[1]])

    def test_boundary_case_empty_list(self):
        self.assertEqual(pack_consecutive_duplicates([]), [])

    def test_boundary_case_all_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1, 1, 1]), [[1, 1, 1, 1]])

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            pack_consecutive_duplicates(123)
