import unittest
from mbpp_97_code import frequency_lists

class TestFrequencyLists(unittest.TestCase):

    def test_normal_input(self):
        self.assertDictEqual(frequency_lists([[1, 2, 2, 3, 3, 3], [4, 4, 4], [5]]), {'1': 1, '2': 2, '3': 3, '4': 3, '5': 1})

    def test_empty_list(self):
        self.assertDictEqual(frequency_lists([]), {})

    def test_single_element_list(self):
        self.assertDictEqual(frequency_lists([[1]]), {'1': 1})

    def test_negative_numbers(self):
        self.assertDictEqual(frequency_lists([[-1, -2, -2, 0, 0, 3]]), {'-1': 1, '-2': 2, '0': 2, '3': 1})

    def test_floating_point_numbers(self):
        self.assertDictEqual(frequency_lists([[1.1, 2.2, 2.2, 3.3, 3.3, 3.3], [4.4, 4.4, 4.4], [5.5]]), {'1.1': 1, '2.2': 2, '3.3': 3, '4.4': 3, '5.5': 1})

    def test_duplicate_lists(self):
        self.assertDictEqual(frequency_lists([[1, 2, 2, 3, 3, 3], [1, 2, 2, 3, 3, 3]]), {'1': 2, '2': 2, '3': 3})

    def test_invalid_input(self):
        self.assertRaises(TypeError, frequency_lists, [1, 'two', 3])
