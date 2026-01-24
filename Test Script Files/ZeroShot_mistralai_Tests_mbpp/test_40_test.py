import unittest
from mbpp_40_code import Counter
from itertools import chain

def freq_element(nums):
  result = Counter(chain.from_iterable(nums))
  return result

class TestFreqElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertDictEqual(freq_element([]), Counter())

    def test_single_element(self):
        self.assertDictEqual(freq_element([1]), Counter({1: 1}))

    def test_multiple_elements(self):
        self.assertDictEqual(freq_element([1, 1, 2, 2, 3, 3, 3]), Counter({1: 2, 2: 2, 3: 3}))

    def test_duplicate_elements(self):
        self.assertDictEqual(freq_element([1, 1, 2, 2, 2, 3, 3, 3, 3, 3]), Counter({1: 2, 2: 3, 3: 4}))
