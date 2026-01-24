import unittest
from mbpp_754_code import extract_index_list

class TestExtractIndexList(unittest.TestCase):
    def test_typical_use_case(self):
        l1 = [1, 2, 3, 4, 5]
        l2 = [1, 2, 3, 4, 5]
        l3 = [1, 2, 3, 4, 5]
        self.assertEqual(extract_index_list(l1, l2, l3), [1, 2, 3, 4, 5])

    def test_edge_condition(self):
        l1 = [1, 2, 3, 4, 5]
        l2 = [1, 2, 3, 4, 6]
        l3 = [1, 2, 3, 4, 5]
        self.assertEqual(extract_index_list(l1, l2, l3), [])

    def test_boundary_condition(self):
        l1 = [1, 2, 3, 4, 5]
        l2 = [1, 2, 3, 4, 5]
        l3 = [1, 2, 3, 4]
        self.assertRaises(ValueError, extract_index_list, l1, l2, l3)

    def test_invalid_input(self):
        l1 = [1, 2, 'a', 4, 5]
        l2 = [1, 2, 3, 4, 5]
        l3 = [1, 2, 3, 4, 5]
        self.assertRaises(TypeError, extract_index_list, l1, l2, l3)
