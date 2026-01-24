import unittest
from mbpp_747_code import lcs_of_three

class TestLCSOfThree(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(lcs_of_three(['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']), 2)
        self.assertEqual(lcs_of_three(['a', 'b', 'c'], ['b', 'a', 'c'], ['c', 'a', 'b']), 2)
        self.assertEqual(lcs_of_three(['a', 'b', 'c'], ['b', 'c', 'a'], ['c', 'a', 'b']), 2)

    def test_edge_and_boundary(self):
        self.assertEqual(lcs_of_three([], [], []), 0)
        self.assertEqual(lcs_of_three(['a'], [], []), 0)
        self.assertEqual(lcs_of_three([], ['a'], []), 0)
        self.assertEqual(lcs_of_three([], [], ['a']), 0)
        self.assertEqual(lcs_of_three(['a'], ['a'], []), 1)
        self.assertEqual(lcs_of_three([], ['a'], ['a']), 0)
        self.assertEqual(lcs_of_three(['a'], [], ['a']), 0)

        self.assertEqual(lcs_of_three(['a', 'b'], ['a', 'b'], ['a', 'c']), 1)
        self.assertEqual(lcs_of_three(['a', 'b'], ['a', 'b'], ['b', 'c']), 1)
        self.assertEqual(lcs_of_three(['a', 'b'], ['a', 'b'], ['c', 'c']), 0)

    def test_complex(self):
        self.assertEqual(lcs_of_three(['a', 'b', 'c', 'd'], ['b', 'c', 'd', 'e'], ['c', 'd', 'e', 'f']), 3)
        self.assertEqual(lcs_of_three(['a', 'b', 'c', 'd'], ['b', 'a', 'c', 'd'], ['c', 'a', 'b', 'd']), 3)
        self.assertEqual(lcs_of_three(['a', 'b', 'c', 'd'], ['b', 'c', 'a', 'd'], ['c', 'a', 'b', 'd']), 3)
