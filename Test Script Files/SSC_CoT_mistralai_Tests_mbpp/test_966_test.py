import unittest
from mbpp_966_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):
    def test_typical_input(self):
        self.assertListEqual(remove_empty((1, 2, 3)), (1, 2, 3))
        self.assertListEqual(remove_empty(('a', 'b', 'c')), ('a', 'b', 'c'))

    def test_edge_cases(self):
        self.assertListEqual(remove_empty([]), [])
        self.assertListEqual(remove_empty((1,)), (1,))
        self.assertListEqual(remove_empty(('',)), [])
        self.assertListEqual(remove_empty((' ',)), [])

    def test_boundary_cases(self):
        self.assertListEqual(remove_empty((1, None)), (1,))
        self.assertListEqual(remove_empty(('a', None)), ('a',))
        self.assertListEqual(remove_empty((1, 0)), (1,))
        self.assertListEqual(remove_empty(('a', '')), ('a',))

    def test_special_cases(self):
        self.assertListEqual(remove_empty((1, 0, None)), (1,))
        self.assertListEqual(remove_empty(('a', '', None)), ('a',))
