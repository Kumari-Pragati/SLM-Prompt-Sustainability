import unittest
from mbpp_142_code import count_samepair

class TestCountSamePair(unittest.TestCase):

    def test_typical_case(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [1, 2, 3, 4, 5]
        list3 = [1, 2, 3, 4, 5]
        self.assertEqual(count_samepair(list1, list2, list3), 5)

    def test_empty_lists(self):
        list1 = []
        list2 = []
        list3 = []
        self.assertEqual(count_samepair(list1, list2, list3), 0)

    def test_different_lists(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [6, 7, 8, 9, 10]
        list3 = [1, 2, 3, 4, 5]
        self.assertEqual(count_samepair(list1, list2, list3), 0)

    def test_unequal_length_lists(self):
        list1 = [1, 2, 3, 4]
        list2 = [1, 2, 3, 4, 5]
        list3 = [1, 2, 3, 4, 5]
        self.assertEqual(count_samepair(list1, list2, list3), 4)

    def test_negative_numbers(self):
        list1 = [-1, -2, -3, -4, -5]
        list2 = [-1, -2, -3, -4, -5]
        list3 = [-1, -2, -3, -4, -5]
        self.assertEqual(count_samepair(list1, list2, list3), 5)

    def test_zeroes(self):
        list1 = [0, 0, 0, 0, 0]
        list2 = [0, 0, 0, 0, 0]
        list3 = [0, 0, 0, 0, 0]
        self.assertEqual(count_samepair(list1, list2, list3), 5)
