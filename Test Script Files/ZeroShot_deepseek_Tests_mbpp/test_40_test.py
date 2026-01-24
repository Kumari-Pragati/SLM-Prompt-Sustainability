import unittest
from mbpp_40_code import Counter
from itertools import chain

def freq_element(nums):
  result = Counter(chain.from_iterable(nums))
  return result

class TestFreqElement(unittest.TestCase):

    def test_single_list(self):
        self.assertEqual(freq_element([[1, 2, 3, 4, 5]]), Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1}))

    def test_multiple_lists(self):
        self.assertEqual(freq_element([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), Counter({1: 1, 2: 2, 3: 3, 4: 2, 5: 1}))

    def test_empty_list(self):
        self.assertEqual(freq_element([]), Counter())

    def test_single_element(self):
        self.assertEqual(freq_element([[1]]), Counter({1: 1}))

    def test_duplicate_elements(self):
        self.assertEqual(freq_element([[1, 1, 1, 2, 2, 3]]), Counter({1: 3, 2: 2, 3: 1}))
