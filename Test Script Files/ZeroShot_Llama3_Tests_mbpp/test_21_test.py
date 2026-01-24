import unittest
from mbpp_21_code import multiples_of_num

class TestMultiplesOfNum(unittest.TestCase):

    def test_multiples_of_num(self):
        self.assertEqual(multiples_of_num(2, 10), [0, 2, 4, 6, 8, 10])
        self.assertEqual(multiples_of_num(3, 15), [0, 3, 6, 9, 12, 15])
        self.assertEqual(multiples_of_num(4, 20), [0, 4, 8, 12, 16, 20])
        self.assertEqual(multiples_of_num(5, 25), [0, 5, 10, 15, 20, 25])
        self.assertEqual(multiples_of_num(1, 5), [0, 1, 2, 3, 4, 5])

    def test_multiples_of_num_edge_cases(self):
        self.assertEqual(multiples_of_num(0, 5), [0, 0, 0, 0, 0, 5])
        self.assertEqual(multiples_of_num(0, 0), [])
