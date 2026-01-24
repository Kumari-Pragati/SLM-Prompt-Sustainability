import unittest
from mbpp_747_code import lcs_of_three

class TestLCSOfThree(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(lcs_of_three(['abc', 'abcd', 'abce'], 4, 4, 4), 3)
        self.assertEqual(lcs_of_three(['cat', 'dog', 'mouse'], 3, 3, 4), 3)

    def test_edge_cases(self):
        self.assertEqual(lcs_of_three([], 0, 0, 0), 0)
        self.assertEqual(lcs_of_three(['a', 'b', 'c'], 3, 0, 0), 0)
        self.assertEqual(lcs_of_three(['a', 'b', 'c'], 0, 3, 0), 0)
        self.assertEqual(lcs_of_three(['a', 'b', 'c'], 0, 0, 3), 0)

    def test_boundary_conditions(self):
        self.assertEqual(lcs_of_three(['aa', 'ab', 'ac'], 3, 3, 1), 2)
        self.assertEqual(lcs_of_three(['aa', 'ab', 'ac'], 3, 2, 1), 2)
        self.assertEqual(lcs_of_three(['aa', 'ab', 'ac'], 2, 3, 1), 2)
        self.assertEqual(lcs_of_three(['aa', 'ab', 'ac'], 2, 2, 2), 2)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, lcs_of_three, ['a', 'b', 'c'], -1, 3, 3)
        self.assertRaises(ValueError, lcs_of_three, ['a', 'b', 'c'], 3, -1, 3)
        self.assertRaises(ValueError, lcs_of_three, ['a', 'b', 'c'], 3, 3, -1)
