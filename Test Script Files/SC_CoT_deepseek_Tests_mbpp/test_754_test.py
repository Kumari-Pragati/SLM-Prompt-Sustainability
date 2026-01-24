import unittest

from mbpp_754_code import extract_index_list

class TestExtractIndexList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_index_list([1, 2, 3], [1, 2, 3], [1, 2, 3]), [1, 2, 3])

    def test_edge_case(self):
        self.assertEqual(extract_index_list([1, 2, 3], [1, 2, 3], [1, 2, 4]), [])

    def test_boundary_case(self):
        self.assertEqual(extract_index_list([1, 2, 3], [1, 2, 3], [1, 2]), [])
        self.assertEqual(extract_index_list([1, 2, 3], [1, 2, 3], [1, 2, 3, 4]), [])

    def test_special_case(self):
        self.assertEqual(extract_index_list([1, 2, 3], [1, 2, 3], [1, 2, 2]), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_index_list([1, 2, 3], [1, 2, 3], 1)

        with self.assertRaises(TypeError):
            extract_index_list([1, 2, 3], 1, [1, 2, 3])

        with self.assertRaises(TypeError):
            extract_index_list(1, [1, 2, 3], [1, 2, 3])
