import unittest
from mbpp_533_code import remove_datatype

class TestRemoveDatatype(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(remove_datatype((1, 2, 3), int), [1, 2, 3])
        self.assertEqual(remove_datatype(('a', 'b', 'c'), str), ['a', 'b', 'c'])

    def test_empty_input(self):
        self.assertEqual(remove_datatype((), int), [])
        self.assertEqual(remove_datatype((), str), [])

    def test_mixed_input(self):
        self.assertEqual(remove_datatype((1, 'a', 2.5), int), [1, 'a', 2.5])
        self.assertEqual(remove_datatype(('a', 1, 2.5), str), ['a', 1, 2.5])

    def test_all_same_type_input(self):
        self.assertEqual(remove_datatype((1, 2, 3), str), [])
        self.assertEqual(remove_datatype(('a', 'b', 'c'), int), [])

    def test_edge_cases(self):
        self.assertEqual(remove_datatype((None, None, None), int), [None, None, None])
        self.assertEqual(remove_datatype((True, False, True), int), [True, False, True])
