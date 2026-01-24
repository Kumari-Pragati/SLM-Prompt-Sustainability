import unittest
from mbpp_853_code import sum_of_odd_Factors

class TestSumOfOddFactors(unittest.TestCase):

    def test_small_prime(self):
        self.assertEqual(sum_of_odd_Factors(7), 7)

    def test_small_composite(self):
        self.assertEqual(sum_of_odd_Factors(12), 2)

    def test_large_prime(self):
        self.assertEqual(sum_of_odd_Factors(23), 23)

    def test_large_composite(self):
        self.assertEqual(sum_of_odd_Factors(36), 2)

    def test_edge_case_one(self):
        self.assertEqual(sum_of_odd_Factors(1), 1)

    def test_edge_case_two(self):
        self.assertEqual(sum_of_odd_Factors(2), 3)

    def test_edge_case_three(self):
        self.assertEqual(sum_of_odd_Factors(3), 3)

    def test_edge_case_four(self):
        self.assertEqual(sum_of_odd_Factors(4), 2)

    def test_edge_case_five(self):
        self.assertEqual(sum_of_odd_Factors(5), 5)

    def test_edge_case_six(self):
        self.assertEqual(sum_of_odd_Factors(6), 2)

    def test_edge_case_seven(self):
        self.assertEqual(sum_of_odd_Factors(7), 7)

    def test_edge_case_eight(self):
        self.assertEqual(sum_of_odd_Factors(8), 2)

    def test_edge_case_nine(self):
        self.assertEqual(sum_of_odd_Factors(9), 3)

    def test_edge_case_ten(self):
        self.assertEqual(sum_of_odd_Factors(10), 2)

    def test_edge_case_eleven(self):
        self.assertEqual(sum_of_odd_Factors(11), 11)

    def test_edge_case_twelve(self):
        self.assertEqual(sum_of_odd_Factors(12), 2)

    def test_edge_case_thirteen(self):
        self.assertEqual(sum_of_odd_Factors(13), 13)

    def test_edge_case_fourteen(self):
        self.assertEqual(sum_of_odd_Factors(14), 2)

    def test_edge_case_fifteen(self):
        self.assertEqual(sum_of_odd_Factors(15), 2)

    def test_edge_case_sixteen(self):
        self.assertEqual(sum_of_odd_Factors(16), 2)

    def test_edge_case_seventeen(self):
        self.assertEqual(sum_of_odd_Factors(17), 17)

    def test_edge_case_eighteen(self):
        self.assertEqual(sum_of_odd_Factors(18), 2)

    def test_edge_case_nineteen(self):
        self.assertEqual(sum_of_odd_Factors(19), 19)

    def test_edge_case_twenty(self):
        self.assertEqual(sum_of_odd_Factors(20), 2)

    def test_edge_case_twenty_one(self):
        self.assertEqual(sum_of_odd_Factors(21), 2)

    def test_edge_case_twenty_two(self):
        self.assertEqual(sum_of_odd_Factors(22), 2)

    def test_edge_case_twenty_three(self):
        self.assertEqual(sum_of_odd_Factors(23), 23)

    def test_edge_case_twenty_four(self):
        self.assertEqual(sum_of_odd_Factors(24), 2)

    def test_edge_case_twenty_five(self):
        self.assertEqual(sum_of_odd_Factors(25), 2)

    def test_edge_case_twenty_six(self):
        self.assertEqual(sum_of_odd_Factors(26), 2)

    def test_edge_case_twenty_seven(self):
        self.assertEqual(sum_of_odd_Factors(27), 3)

    def test_edge_case_twenty_eight(self):
        self.assertEqual(sum_of_odd_Factors(28), 2)

    def test_edge_case_twenty_nine(self):
        self.assertEqual(sum_of_odd_Factors(29), 29)

    def test_edge_case_thirty(self):
        self.assertEqual(sum_of_odd_Factors(30), 2)

    def test_edge_case_thirty_one(self):
        self.assertEqual(sum_of_odd_Factors(31), 31)

    def test_edge_case_thirty_two(self):
        self.assertEqual(sum_of_odd_Factors(32), 2)

    def test_edge_case_thirty_three(self):
        self.assertEqual(sum_of_odd_Factors(33), 3)

    def test_edge_case_thirty_four(self):
        self.assertEqual(sum_of_odd_Factors(34), 2)

    def test_edge_case_thirty_five(self):
        self.assertEqual(sum_of_odd_Factors(35), 2)

    def test_edge_case_thirty_six(self):
        self.assertEqual(sum_of_odd_Factors(36), 2)

    def test_edge_case_thirty_seven(self):
        self.assertEqual(sum_of_odd_Factors(37), 37)

    def test_edge_case_thirty_eight(self):
        self.assertEqual(sum_of_odd_Factors(38), 2)

    def test_edge_case_thirty_nine(self):
        self.assertEqual(sum