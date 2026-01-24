import unittest
from mbpp_40_code import Counter
from itertools import chain
from 40_code import freq_element

class TestFreqElement(unittest.TestCase):
    def test_normal_input(self):
        self.assertCountEqual(freq_element([1, 2, 2, 3, 3, 3]), Counter({1: 1, 2: 2, 3: 3}))
        self.assertCountEqual(freq_element([4, 4, 4, 5, 5, 5]), Counter({4: 3, 5: 3}))

    def test_edge_and_boundary_conditions(self):
        self.assertCountEqual(freq_element([]), Counter())
        self.assertCountEqual(freq_element([1]), Counter({1: 1}))
        self.assertCountEqual(freq_element([1, 1, 1, 1, 1]), Counter({1: 4}))
        self.assertCountEqual(freq_element([float('inf'), float('inf'), float('inf'), -1]), Counter({float('inf'): 3, -1: 1}))

    def test_special_or_corner_cases(self):
        self.assertCountEqual(freq_element([1, 2, 3, 2]), Counter({1: 1, 2: 2, 3: 1}))
        self.assertCountEqual(freq_element([1, 1, 1, 2, 2, 2]), Counter({1: 3, 2: 3}))
        self.assertCountEqual(freq_element([1, 1.0, 1]), Counter({1: 2, 1.0: 1}))
