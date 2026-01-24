import unittest
from mbpp_745_code import divisible_by_digits

class TestDivisibleByDigits(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertCountEqual(divisible_by_digits(1234, 5678), [1234, 1235, 1236, 1237, 5674, 5675, 5676, 5677, 5678])
        self.assertCountEqual(divisible_by_digits(10, 100), [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90])
        self.assertCountEqual(divisible_by_digits(1000, 10000), [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 3000, 4000, 5000, 6000, 7000, 8000, 9000])

    def test_edge_and_boundary_conditions(self):
        self.assertCountEqual(divisible_by_digits(0, 1), [])
        self.assertCountEqual(divisible_by_digits(1, 0), [])
        self.assertCountEqual(divisible_by_digits(1, 1), [1])
        self.assertCountEqual(divisible_by_digits(1, 2), [1])
        self.assertCountEqual(divisible_by_digits(2, 1), [])
        self.assertCountEqual(divisible_by_digits(10, 9), [10])
        self.assertCountEqual(divisible_by_digits(9, 10), [9])
        self.assertCountEqual(divisible_by_digits(100, 99), [100])

    def test_special_cases(self):
        self.assertCountEqual(divisible_by_digits(1111, 2222), [])
        self.assertCountEqual(divisible_by_digits(2222, 3333), [2222])
        self.assertCountEqual(divisible_by_digits(3333, 4444), [3333])
        self.assertCountEqual(divisible_by_digits(4444, 5555), [4444, 5554])
