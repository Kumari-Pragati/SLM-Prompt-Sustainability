import unittest
from mbpp_40_code import freq_element

class TestFreqElement(unittest.TestCase):

    def test_simple(self):
        self.assertDictEqual(freq_element([1, 2, 2, 3, 3, 3]), {'1': 1, '2': 2, '3': 3})
        self.assertDictEqual(freq_element([4, 4, 4, 4]), {'4': 4})
        self.assertDictEqual(freq_element([5, 5, 6, 6, 6]), {'5': 1, '6': 3})

    def test_edge_and_boundary(self):
        self.assertDictEqual(freq_element([]), {})
        self.assertDictEqual(freq_element([0]), {'0': 1})
        self.assertDictEqual(freq_element([1000000000]), {'1000000000': 1})
        self.assertDictEqual(freq_element([1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]), {'1': 3, '2': 2, '3': 3, '4': 4, '5': 1})
