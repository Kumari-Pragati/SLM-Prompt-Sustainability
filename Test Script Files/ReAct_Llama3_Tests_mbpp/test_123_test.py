import unittest
from mbpp_123_code import amicable_numbers_sum

class TestAmicableNumbersSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(amicable_numbers_sum(10000), 31626)

    def test_edge_case_limit_zero(self):
        with self.assertRaises(ValueError):
            amicable_numbers_sum(0)

    def test_edge_case_limit_one(self):
        with self.assertRaises(ValueError):
            amicable_numbers_sum(1)

    def test_edge_case_limit_two(self):
        self.assertEqual(amicable_numbers_sum(2), 0)

    def test_edge_case_limit_three(self):
        self.assertEqual(amicable_numbers_sum(3), 0)

    def test_edge_case_limit_four(self):
        self.assertEqual(amicable_numbers_sum(4), 0)

    def test_edge_case_limit_five(self):
        self.assertEqual(amicable_numbers_sum(5), 0)

    def test_edge_case_limit_six(self):
        self.assertEqual(amicable_numbers_sum(6), 0)

    def test_edge_case_limit_seven(self):
        self.assertEqual(amicable_numbers_sum(7), 0)

    def test_edge_case_limit_eight(self):
        self.assertEqual(amicable_numbers_sum(8), 0)

    def test_edge_case_limit_nine(self):
        self.assertEqual(amicable_numbers_sum(9), 0)

    def test_edge_case_limit_ten(self):
        self.assertEqual(amicable_numbers_sum(10), 0)

    def test_edge_case_limit_eleven(self):
        self.assertEqual(amicable_numbers_sum(11), 0)

    def test_edge_case_limit_twelve(self):
        self.assertEqual(amicable_numbers_sum(12), 0)

    def test_edge_case_limit_thirteen(self):
        self.assertEqual(amicable_numbers_sum(13), 0)

    def test_edge_case_limit_fourteen(self):
        self.assertEqual(amicable_numbers_sum(14), 0)

    def test_edge_case_limit_fifteen(self):
        self.assertEqual(amicable_numbers_sum(15), 0)

    def test_edge_case_limit_sixteen(self):
        self.assertEqual(amicable_numbers_sum(16), 0)

    def test_edge_case_limit_seventeen(self):
        self.assertEqual(amicable_numbers_sum(17), 0)

    def test_edge_case_limit_eighteen(self):
        self.assertEqual(amicable_numbers_sum(18), 0)

    def test_edge_case_limit_nineteen(self):
        self.assertEqual(amicable_numbers_sum(19), 0)

    def test_edge_case_limit_twenty(self):
        self.assertEqual(amicable_numbers_sum(20), 0)

    def test_edge_case_limit_twenty_one(self):
        self.assertEqual(amicable_numbers_sum(21), 0)

    def test_edge_case_limit_twenty_two(self):
        self.assertEqual(amicable_numbers_sum(22), 0)

    def test_edge_case_limit_twenty_three(self):
        self.assertEqual(amicable_numbers_sum(23), 0)

    def test_edge_case_limit_twenty_four(self):
        self.assertEqual(amicable_numbers_sum(24), 0)

    def test_edge_case_limit_twenty_five(self):
        self.assertEqual(amicable_numbers_sum(25), 0)

    def test_edge_case_limit_twenty_six(self):
        self.assertEqual(amicable_numbers_sum(26), 0)

    def test_edge_case_limit_twenty_seven(self):
        self.assertEqual(amicable_numbers_sum(27), 0)

    def test_edge_case_limit_twenty_eight(self):
        self.assertEqual(amicable_numbers_sum(28), 0)

    def test_edge_case_limit_twenty_nine(self):
        self.assertEqual(amicable_numbers_sum(29), 0)

    def test_edge_case_limit_thirty(self):
        self.assertEqual(amicable_numbers_sum(30), 0)

    def test_edge_case_limit_thirty_one(self):
        self.assertEqual(amicable_numbers_sum(31), 0)

    def test_edge_case_limit_thirty_two(self):
        self.assertEqual(amicable_numbers_sum(32), 0)

    def test_edge_case_limit_thirty_three(self):
        self.assertEqual(amicable_numbers_sum(33), 0)

    def test_edge_case_limit_thirty_four(self):
        self.assertEqual(amicable_numbers_sum(34), 0)

    def test_edge_case_limit_thirty_five(self):
        self.assertEqual(amicable_numbers_sum(35), 0)

    def test_edge_case_limit_thirty_six(self):
        self.assertEqual(amicable_numbers_sum(36), 0)

    def test_edge_case_limit_thirty_seven(self):
        self.assertEqual(amicable_numbers_sum(37), 0)

    def test_edge_case_limit_thirty_eight(self):
        self.assertEqual(amicable_numbers_sum(38), 0)

    def test_edge_case_limit_thirty_nine(self):
        self.assertEqual(amic