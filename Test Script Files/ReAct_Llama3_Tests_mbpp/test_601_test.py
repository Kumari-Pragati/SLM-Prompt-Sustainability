import unittest
from mbpp_601_code import max_chain_length

class TestMaxChainLength(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(max_chain_length([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(max_chain_length([Pair(1, 2)], 1), 1)

    def test_two_elements_array(self):
        self.assertEqual(max_chain_length([Pair(1, 2), Pair(2, 3)], 2), 2)

    def test_three_elements_array(self):
        self.assertEqual(max_chain_length([Pair(1, 2), Pair(2, 3), Pair(3, 4)], 3), 3)

    def test_chain_of_length_4(self):
        self.assertEqual(max_chain_length([Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(4, 5)], 4), 4)

    def test_chain_of_length_5(self):
        self.assertEqual(max_chain_length([Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(4, 5), Pair(5, 6)], 5), 5)

    def test_chain_of_length_6(self):
        self.assertEqual(max_chain_length([Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(4, 5), Pair(5, 6), Pair(6, 7)], 6), 6)

    def test_chain_of_length_7(self):
        self.assertEqual(max_chain_length([Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(4, 5), Pair(5, 6), Pair(6, 7), Pair(7, 8)], 7), 7)

    def test_chain_of_length_8(self):
        self.assertEqual(max_chain_length([Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(4, 5), Pair(5, 6), Pair(6, 7), Pair(7, 8), Pair(8, 9)], 8), 8)

    def test_chain_of_length_9(self):
        self.assertEqual(max_chain_length([Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(4, 5), Pair(5, 6), Pair(6, 7), Pair(7, 8), Pair(8, 9), Pair(9, 10)], 9), 9)

    def test_chain_of_length_10(self):
        self.assertEqual(max_chain_length([Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(4, 5), Pair(5, 6), Pair(6, 7), Pair(7, 8), Pair(8, 9), Pair(9, 10), Pair(10, 11)], 10), 10)

    def test_chain_of_length_11(self):
        self.assertEqual(max_chain_length([Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(4, 5), Pair(5, 6), Pair(6, 7), Pair(7, 8), Pair(8, 9), Pair(9, 10), Pair(10, 11), Pair(11, 12)], 11), 11)

    def test_chain_of_length_12(self):
        self.assertEqual(max_chain_length([Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(4, 5), Pair(5, 6), Pair(6, 7), Pair(7, 8), Pair(8, 9), Pair(9, 10), Pair(10, 11), Pair(11, 12), Pair(12, 13)], 12), 12)

    def test_chain_of_length_13(self):
        self.assertEqual(max_chain_length([Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(4, 5), Pair(5, 6), Pair(6, 7), Pair(7, 8), Pair(8, 9), Pair(9, 10), Pair(10, 11), Pair(11, 12), Pair(12, 13), Pair(13, 14)], 13), 13)

    def test_chain_of_length_14(self):
        self.assertEqual(max_chain_length([Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(4, 5), Pair(5, 6),