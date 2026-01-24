import unittest
from mbpp_317_code import groupby

def modified_encode(alist):
    def ctr_ele(el):
        if len(el)>1: return [len(el), el[0]]
        else: return el[0]
    return [ctr_ele(list(group)) for key, group in groupby(alist)]

class TestModifiedEncode(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(modified_encode([]), [])

    def test_single_element_list(self):
        self.assertEqual(modified_encode([1]), [1])

    def test_list_with_single_element_groups(self):
        self.assertEqual(modified_encode([1, 1, 2, 1, 2, 2]), [1, 1, [2, 1], 2, 2])

    def test_list_with_multiple_element_groups(self):
        self.assertEqual(modified_encode([1, 1, 1, 2, 2, 2, 3, 3, 3]), [3, 3, 3, [2, 2], [2, 2], 3])
