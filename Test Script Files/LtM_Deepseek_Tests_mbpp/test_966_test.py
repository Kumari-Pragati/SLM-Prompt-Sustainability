import unittest
from mbpp_966_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(remove_empty([(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]), [('',), ('a', 'b'), ('a', 'b', 'c'), ('d')])

    def test_edge_conditions(self):
        self.assertEqual(remove_empty([]), [])
        self.assertEqual(remove_empty([(), ()]), [])
        self.assertEqual(remove_empty([('',), ('',)]), [('',)])

    def test_complex_cases(self):
        self.assertEqual(remove_empty([('',), (), ('a', 'b'), ('a', 'b', 'c'), ('d')]), [('',), ('a', 'b'), ('a', 'b', 'c'), ('d')])
        self.assertEqual(remove_empty([(), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]), [('',), ('a', 'b'), ('a', 'b', 'c'), ('d')])
