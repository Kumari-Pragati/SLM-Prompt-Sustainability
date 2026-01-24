import unittest
from mbpp_533_code import remove_datatype

class TestRemoveDatatype(unittest.TestCase):

    def test_typical_case_int(self):
        self.assertEqual(remove_datatype((1, 2, 3, 4), int), [1, 2, 3, 4])

    def test_typical_case_str(self):
        self.assertEqual(remove_datatype(('a', 'b', 'c', 'd'), str), ['a', 'b', 'c', 'd'])

    def test_edge_case_empty_tuple(self):
        self.assertEqual(remove_datatype((), int), [])

    def test_boundary_case_mixed_types(self):
        self.assertEqual(remove_datatype((1, 'a', 2.0, None), int), [1, 'a', 2.0, None])

    def test_corner_case_all_same_type(self):
        self.assertEqual(remove_datatype((1, 1, 1, 1), int), [])

    def test_corner_case_all_different_types(self):
        self.assertEqual(remove_datatype((1, 'a', 2.0, None), str), ['a'])
