import unittest
from mbpp_966_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(remove_empty([(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]), [('',), ('a', 'b'), ('a', 'b', 'c'), ('d')])

    def test_edge_cases(self):
        self.assertEqual(remove_empty([(), ('a', 'b'), ('a', 'b', 'c'), ('d')]), [('a', 'b'), ('a', 'b', 'c'), ('d')])
        self.assertEqual(remove_empty([(), (), ()]), [])

    def test_corner_cases(self):
        self.assertEqual(remove_empty([(), ('a',), ('a', 'b'), ()]), [('a',), ('a', 'b')])
