import unittest
from mbpp_747_code import lcs_of_three

class TestLcsOfThree(unittest.TestCase):
    def test_lcs_of_three_typical_use_case(self):
        self.assertEqual(lcs_of_three(['abc', 'bcd', 'abcd'], 3, 3, 4), 3)
        self.assertEqual(lcs_of_three(['a', 'b', 'ab'], 2, 2, 3), 1)
        self.assertEqual(lcs_of_three(['', 'a', 'ab'], 1, 2, 3), 0)
        self.assertEqual(lcs_of_three(['abc', 'bcd', 'efg'], 3, 3, 4), 0)
        self.assertEqual(lcs_of_three(['', '', ''], 0, 0, 0), 0)
        self.assertEqual(lcs_of_three(['abc', '', 'def'], 3, 0, 4), 0)
        self.assertEqual(lcs_of_three(['abc', 'bcd', ''], 3, 3, 0), 0)
        self.assertEqual(lcs_of_three(['', 'bcd', 'def'], 0, 3, 4), 0)
        self.assertEqual(lcs_of_three(['abc', 'bcd', 'def'], 3, 3, 5), 0)
