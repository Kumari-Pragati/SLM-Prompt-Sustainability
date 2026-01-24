import unittest
from mbpp_21_code import multiples_of_num

class TestMultiplesOfNum(unittest.TestCase):

    def test_multiples_of_num(self):
        self.assertEqual(multiples_of_num(3, 5), [5, 10, 15])
        self.assertEqual(multiples_of_num(4, 7), [28, 35, 42, 49])
        self.assertEqual(multiples_of_num(2, 10), [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
        self.assertEqual(multiples_of_num(0, 10), [])
        self.assertEqual(multiples_of_num(1, 0), [])
        self.assertEqual(multiples_of_num(0, 0), [])
