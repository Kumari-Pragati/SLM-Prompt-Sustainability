import unittest
from mbpp_40_code import freq_element

class TestFreqElement(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(freq_element([[1, 2, 3], [2, 3, 4]]), Counter({1: 1, 2: 2, 3: 2, 4: 1}))

    def test_empty_input(self):
        self.assertEqual(freq_element([]), Counter())

    def test_single_element_input(self):
        self.assertEqual(freq_element([[1]]), Counter({1: 1}))

    def test_duplicate_elements_input(self):
        self.assertEqual(freq_element([[1, 1, 2, 2], [2, 2, 3, 3]]), Counter({1: 2, 2: 4, 3: 2}))

    def test_large_input(self):
        self.assertEqual(freq_element([list(range(1, 1001))]), Counter({1: 1000}))

    def test_negative_numbers_input(self):
        self.assertEqual(freq_element([[-1, -1, 1, 1]]), Counter({-1: 2, 1: 2}))
