import unittest
from mbpp_754_code import extract_index_list

class TestExtractIndexList(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(extract_index_list([1, 2, 3], [1, 2, 3], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(extract_index_list([1, 2, 3], [1, 2, 4], [1, 2, 3]), [1, 2])

    def test_edge_conditions(self):
        self.assertEqual(extract_index_list([], [], []), [])
        self.assertEqual(extract_index_list([1], [1], [2]), [])

    def test_complex_cases(self):
        self.assertEqual(extract_index_list([1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(extract_index_list([1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 4]), [1, 2, 3])
