import unittest
from mbpp_40_code import freq_element

class TestFreqElement(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(freq_element([]), {})

    def test_single_element(self):
        self.assertEqual(freq_element([[1]]), {1: 1})

    def test_multiple_elements(self):
        self.assertEqual(freq_element([[1, 2], [2, 3]]), {1: 1, 2: 2, 3: 1})

    def test_empty_sublist(self):
        self.assertEqual(freq_element([[], [1, 2]]), {1: 1, 2: 1})

    def test_repeated_elements(self):
        self.assertEqual(freq_element([[1, 1, 2, 2, 3, 3]]), {1: 2, 2: 2, 3: 2})

    def test_negative_numbers(self):
        self.assertEqual(freq_element([[-1, -2, 1, 2]]), {-1: 1, -2: 1, 1: 1, 2: 1})

    def test_large_numbers(self):
        self.assertEqual(freq_element([[100, 200, 300]]), {100: 1, 200: 1, 300: 1})
