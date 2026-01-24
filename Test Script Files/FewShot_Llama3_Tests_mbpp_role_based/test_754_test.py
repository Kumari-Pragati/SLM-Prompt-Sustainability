import unittest
from mbpp_754_code import extract_index_list

class TestExtractIndexList(unittest.TestCase):
    def test_common_elements(self):
        l1 = [1, 2, 3]
        l2 = [1, 2, 3]
        l3 = [1, 2, 3]
        self.assertEqual(extract_index_list(l1, l2, l3), [1, 2, 3])

    def test_no_common_elements(self):
        l1 = [1, 2, 3]
        l2 = [4, 5, 6]
        l3 = [7, 8, 9]
        self.assertEqual(extract_index_list(l1, l2, l3), [])

    def test_common_elements_at_start(self):
        l1 = [1, 2, 3]
        l2 = [1, 2, 3]
        l3 = [1, 2, 4]
        self.assertEqual(extract_index_list(l1, l2, l3), [1, 2])

    def test_common_elements_at_end(self):
        l1 = [1, 2, 3]
        l2 = [1, 2, 3]
        l3 = [1, 2, 3]
        self.assertEqual(extract_index_list(l1, l2, l3), [1, 2, 3])

    def test_common_elements_at_middle(self):
        l1 = [1, 2, 3]
        l2 = [1, 2, 3]
        l3 = [1, 3, 3]
        self.assertEqual(extract_index_list(l1, l2, l3), [1, 2, 3])
