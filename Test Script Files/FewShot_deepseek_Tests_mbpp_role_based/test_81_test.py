import unittest
from mbpp_81_code import zip_tuples

class TestZipTuples(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(zip_tuples(('a', 'b', 'c'), (1, 2, 3)), [('a', 1), ('b', 2), ('c', 3)])

    def test_edge_condition(self):
        self.assertEqual(zip_tuples((), (1, 2, 3)), [])

    def test_boundary_condition(self):
        self.assertEqual(zip_tuples(('a', 'b', 'c'), ()), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            zip_tuples('a', 'b')
