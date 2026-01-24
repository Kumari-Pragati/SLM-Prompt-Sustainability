import unittest
from mbpp_109_code import odd_Equivalent

class TestOddEquivalent(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(odd_Equivalent('111', 3), 3)

    def test_edge_case_zero_length(self):
        self.assertEqual(odd_Equivalent('', 3), 0)

    def test_edge_case_zero_input(self):
        self.assertEqual(odd_Equivalent('111', 0), 0)

    def test_edge_case_single_digit(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)

    def test_edge_case_single_digit_zero(self):
        self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_edge_case_single_digit_one(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)

    def test_edge_case_single_digit_two(self):
        self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_edge_case_single_digit_three(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)

    def test_edge_case_single_digit_four(self):
        self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_edge_case_single_digit_five(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)

    def test_edge_case_single_digit_six(self):
        self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_edge_case_single_digit_seven(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)

    def test_edge_case_single_digit_eight(self):
        self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_edge_case_single_digit_nine(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)

    def test_edge_case_single_digit_ten(self):
        self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_edge_case_single_digit_eleven(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)

    def test_edge_case_single_digit_twelve(self):
        self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_edge_case_single_digit_thirteen(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)

    def test_edge_case_single_digit_fourteen(self):
        self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_edge_case_single_digit_fifteen(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)

    def test_edge_case_single_digit_sixteen(self):
        self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_edge_case_single_digit_seventeen(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)

    def test_edge_case_single_digit_eighteen(self):
        self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_edge_case_single_digit_nineteen(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)

    def test_edge_case_single_digit_twenty(self):
        self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_edge_case_single_digit_twentyone(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)

    def test_edge_case_single_digit_twentytwo(self):
        self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_edge_case_single_digit_twentythree(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)

    def test_edge_case_single_digit_twentyfour(self):
        self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_edge_case_single_digit_twentyfive(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)

    def test_edge_case_single_digit_twenty_six(self):
        self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_edge_case_single_digit_twenty_seven(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)

    def test_edge_case_single_digit_twenty_eight(self):
        self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_edge_case_single_digit_twenty_nine(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)

    def test_edge_case_single_digit_thirty(self):
        self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_edge_case_single_digit_thirtyone(self):
        self.assertEqual(odd_Equivalent('1',