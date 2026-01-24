import unittest
from mbpp_691_code import groupby

def group_element(test_list):
  res = dict()
  for key, val in groupby(sorted(test_list, key = lambda ele: ele[1]), key = lambda ele: ele[1]):
    res[key] = [ele[0] for ele in val]
  return (res)

class TestGroupElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertDictEqual(group_element([]), {})

    def test_single_element(self):
        self.assertDictEqual(group_element([(1, 1)]), {'1': [(1, 1)]})

    def test_multiple_elements(self):
        self.assertDictEqual(group_element([(1, 1), (2, 2), (1, 1), (3, 3), (2, 2), (1, 1)]), {'1': [(1, 1), (1, 1), (1, 1)], '2': [(2, 2), (2, 2)], '3': [(3, 3)]})
