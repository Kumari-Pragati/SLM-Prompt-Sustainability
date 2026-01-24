import unittest
from mbpp_97_code import frequency_lists

class TestFrequencyLists(unittest.TestCase):

    def test_empty_list(self):
        self.assertDictEqual(frequency_lists([]), {})

    def test_single_element_list(self):
        self.assertDictEqual(frequency_lists([[1]]), {1: 1})

    def test_multiple_elements_list(self):
        self.assertDictEqual(frequency_lists([[1, 2], [2, 3], [1, 2, 3]]), {1: 2, 2: 2, 3: 1})

    def test_duplicate_elements_list(self):
        self.assertDictEqual(frequency_lists([[1, 1], [2, 2, 2], [3, 3]]), {1: 2, 2: 3, 3: 2})

    def test_negative_numbers(self):
        self.assertDictEqual(frequency_lists([[-1, -2], [0, -3], [1, -2]]), {-1: 1, -2: 2, -3: 1, 0: 1})

    def test_zero(self):
        self.assertDictEqual(frequency_lists([[0], [0, 0], [0, 0, 0]]), {0: 3})

    def test_invalid_input(self):
        self.assertRaises(TypeError, frequency_lists, [1, "two"])
