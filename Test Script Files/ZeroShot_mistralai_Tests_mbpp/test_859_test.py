import unittest
from mbpp_859_code import combinations

def sub_lists(my_list):
    subs = []
    for i in range(0, len(my_list)+1):
        temp = [list(x) for x in combinations(my_list, i)]
        if len(temp)>0:
            subs.extend(temp)
    return subs

class TestSubLists(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sub_lists([]), [[]])

    def test_single_element_list(self):
        self.assertEqual(sub_lists([1]), [[1]])

    def test_two_element_list(self):
        self.assertEqual(sub_lists([1, 2]), [[1], [2], [1, 2]])

    def test_three_element_list(self):
        self.assertEqual(sub_lists([1, 2, 3]), [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])

    def test_four_element_list(self):
        self.assertEqual(sub_lists([1, 2, 3, 4]), [[1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]])
