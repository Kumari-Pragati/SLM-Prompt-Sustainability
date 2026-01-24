import unittest
from mbpp_114_code import Counter

def assign_freq(test_list):
  res = [(*key, val) for key, val in Counter(test_list).items()]
  return (str(res))

class TestAssignFreq(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(assign_freq([]), '[]')

    def test_single_element(self):
        self.assertEqual(assign_freq(['a']), '["a": 1]')

    def test_multiple_elements(self):
        self.assertEqual(assign_freq(['a', 'b', 'a', 'c', 'b']), '["a": 2, "b": 2, "c": 1]')

    def test_duplicate_strings_and_numbers(self):
        self.assertEqual(assign_freq(['a', 1, 'a', 1, 'b', 2, 'b', 2, 'a']), '["a": 3, "1": 2, "b": 2, "2": 2]')
