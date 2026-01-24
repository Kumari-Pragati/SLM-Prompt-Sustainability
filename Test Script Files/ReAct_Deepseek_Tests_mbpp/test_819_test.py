import unittest
from mbpp_819_code import count_duplic

class TestCountDuplic(unittest.TestCase):

    def test_typical_case(self):
        lists = [1, 1, 2, 2, 3, 3, 4, 4]
        expected_element = [1, 2, 3, 4]
        expected_frequency = [2, 2, 2, 2]
        self.assertEqual(count_duplic(lists), (expected_element, expected_frequency))

    def test_single_element(self):
        lists = [1]
        expected_element = [1]
        expected_frequency = [1]
        self.assertEqual(count_duplic(lists), (expected_element, expected_frequency))

    def test_empty_list(self):
        lists = []
        expected_element = []
        expected_frequency = []
        self.assertEqual(count_duplic(lists), (expected_element, expected_frequency))

    def test_repeated_elements(self):
        lists = [1, 1, 1, 1]
        expected_element = [1]
        expected_frequency = [4]
        self.assertEqual(count_duplic(lists), (expected_element, expected_frequency))

    def test_no_duplicates(self):
        lists = [1, 2, 3, 4]
        expected_element = [1, 2, 3, 4]
        expected_frequency = [1, 1, 1, 1]
        self.assertEqual(count_duplic(lists), (expected_element, expected_frequency))

    def test_mixed_elements(self):
        lists = [1, 2, 2, 3, 3, 4, 4, 4]
        expected_element = [1, 2, 3, 4]
        expected_frequency = [1, 2, 2, 3]
        self.assertEqual(count_duplic(lists), (expected_element, expected_frequency))
