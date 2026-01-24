import unittest
from mbpp_966_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertEqual(remove_empty([]), [])

    def test_empty_list(self):
        self.assertEqual(remove_empty([None, '', [], (), (), ('',)]), [])

    def test_single_empty_string(self):
        self.assertEqual(remove_empty(['',]), [''])

    def test_single_empty_list(self):
        self.assertEqual(remove_empty([['',]]), [['']])

    def test_single_empty_tuple(self):
        self.assertEqual(remove_empty([(), ('',)]), [()])

    def test_multiple_empty_elements(self):
        self.assertEqual(remove_empty([('',), ('a', 'b'), ('',), ('a', 'b', 'c'), ('d'), ('',)]), [('a', 'b'), ('a', 'b', 'c'), ('d')])
