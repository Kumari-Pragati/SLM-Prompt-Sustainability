import unittest
from mbpp_361_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(remove_empty([1, 2, '', 3, None, 'a']), [1, 2, 3, 'a'])
        self.assertEqual(remove_empty(['a', 'b', 'c']), ['a', 'b', 'c'])

    def test_edge_cases(self):
        self.assertEqual(remove_empty([None]), [])
        self.assertEqual(remove_empty(['']), [])
        self.assertEqual(remove_empty([]), [])

    def test_boundary_conditions(self):
        self.assertEqual(remove_empty(['a', None, 'b']), ['a', 'b'])
        self.assertEqual(remove_empty([None, 'a', None]), ['a'])

    def test_corner_cases(self):
        self.assertEqual(remove_empty(['', '', '']), [])
        self.assertEqual(remove_empty([None, None, None]), [])
