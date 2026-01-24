import unittest
from mbpp_966_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_empty([(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]), [('',), ('a', 'b'), ('a', 'b', 'c'), ('d')])

    def test_empty_tuple(self):
        self.assertEqual(remove_empty([(), ()]), [])

    def test_single_non_empty_tuple(self):
        self.assertEqual(remove_empty([('a', 'b')]), [('a', 'b')])

    def test_all_empty_tuples(self):
        self.assertEqual(remove_empty([(), (), ()]), [])

    def test_empty_and_non_empty_tuples(self):
        self.assertEqual(remove_empty([(), ('a', 'b')]), [('a', 'b')])

    def test_single_empty_tuple(self):
        self.assertEqual(remove_empty([()]), [])

    def test_single_non_empty_tuple_with_string(self):
        self.assertEqual(remove_empty([('a',)]), [('a',)])

    def test_empty_and_single_non_empty_tuple(self):
        self.assertEqual(remove_empty([(), ('a',)]), [('a',)])

    def test_single_tuple_with_multiple_elements(self):
        self.assertEqual(remove_empty([('a', 'b', 'c')]), [('a', 'b', 'c')])

    def test_empty_and_single_tuple_with_multiple_elements(self):
        self.assertEqual(remove_empty([(), ('a', 'b', 'c')]), [('a', 'b', 'c')])

    def test_empty_and_single_empty_tuple_with_multiple_elements(self):
        self.assertEqual(remove_empty([(), ()]), [])

    def test_empty_and_single_empty_tuple_with_single_element(self):
        self.assertEqual(remove_empty([(), ()]), [])
