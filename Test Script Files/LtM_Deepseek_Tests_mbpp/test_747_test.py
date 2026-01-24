import unittest
from mbpp_747_code import lcs_of_three

class TestLCSOfThree(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(lcs_of_three('ABCDGH', 'AEDFHR', 'ADHMNR', 6, 6, 6), 3)

    def test_edge_conditions(self):
        self.assertEqual(lcs_of_three('', 'AEDFHR', 'ADHMNR', 0, 6, 6), 0)
        self.assertEqual(lcs_of_three('ABCDGH', '', 'ADHMNR', 6, 0, 6), 0)
        self.assertEqual(lcs_of_three('ABCDGH', 'AEDFHR', '', 6, 6, 0), 0)
        self.assertEqual(lcs_of_three('', '', '', 0, 0, 0), 0)

    def test_boundary_conditions(self):
        self.assertEqual(lcs_of_three('A'*10000, 'A'*10000, 'A'*10000, 10000, 10000, 10000), 10000)
        self.assertEqual(lcs_of_three('A'*10001, 'A'*10001, 'A'*10001, 10001, 10001, 10001), 10001)

    def test_complex_cases(self):
        self.assertEqual(lcs_of_three('ABCDEF', 'ZXBCDE', 'ZYBCDEF', 6, 6, 7), 6)
        self.assertEqual(lcs_of_three('ABCDEF', 'ABCDEF', 'ABCDEF', 6, 6, 6), 6)
