import unittest
from mbpp_21_code import multiples_of_num

class TestMultiplesOfNum(unittest.TestCase):

    def test_simple_multiples(self):
        self.assertListEqual(multiples_of_num(5, 3), [3, 6, 9, 12, 15])
        self.assertListEqual(multiples_of_num(10, 5), [5, 10, 15, 20, 25])

    def test_edge_cases(self):
        self.assertListEqual(multiples_of_num(0, 4), [])
        self.assertListEqual(multiples_of_num(1, 2), [2])
        self.assertListEqual(multiples_of_num(1, 1), [1])
        self.assertListEqual(multiples_of_num(2, 1), [])

    def test_boundary_conditions(self):
        self.assertListEqual(multiples_of_num(1, 2), [2])
        self.assertListEqual(multiples_of_num(2, 1), [])
        self.assertListEqual(multiples_of_num(0, 4), [])
        self.assertListEqual(multiples_of_num(1, 0), [])

    def test_negative_numbers(self):
        self.assertListEqual(multiples_of_num(-3, 2), [-2, -4, -6])
        self.assertListEqual(multiples_of_num(-5, -3), [3, -6, -9])

    def test_large_numbers(self):
        self.assertListEqual(multiples_of_num(100, 7), [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98])
        self.assertListEqual(multiples_of_num(1000, 17), [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255, 272, 289, 306, 323, 340, 357, 374, 391, 408, 425, 442, 459, 476, 493, 510, 527, 544, 561, 578, 595, 612, 629, 646, 663, 680, 697, 714, 731, 748, 765, 782, 799])
