import unittest
from mbpp_966_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_empty([(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]), [('',), ('a', 'b'), ('a', 'b', 'c'), ('d')])

    def test_empty_tuple(self):
        self.assertEqual(remove_empty([(), ()]), [()])

    def test_single_non_empty_tuple(self):
        self.assertEqual(remove_empty([('a', 'b')]), [('a', 'b')])

    def test_all_empty_tuples(self):
        self.assertEqual(remove_empty([(), ()]), [()])

    def test_empty_input(self):
        self.assertEqual(remove_empty([]), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_empty(123)
