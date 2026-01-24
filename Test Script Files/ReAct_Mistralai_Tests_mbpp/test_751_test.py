import unittest
from mbpp_751_code import check_min_heap

class TestCheckMinHeap(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(check_min_heap([]))

    def test_single_element(self):
        for element in [1]:
            self.assertTrue(check_min_heap(element))

    def test_two_elements(self):
        for left, right in [(1, 2), (2, 1), (1, 1)]:
            self.assertTrue(check_min_heap([left, right]))

    def test_three_elements(self):
        for left, mid, right in [
            (1, 2, 3), (2, 1, 3), (1, 3, 2), (3, 1, 2), (3, 2, 1)
        ]:
            self.assertTrue(check_min_heap([left, mid, right]))

    def test_four_elements(self):
        for left, mid1, mid2, right in [
            (1, 2, 3, 4), (2, 1, 3, 4), (1, 3, 2, 4), (3, 1, 2, 4),
            (3, 2, 1, 4), (4, 1, 2, 3), (4, 2, 1, 3), (4, 3, 1, 2)
        ]:
            self.assertTrue(check_min_heap([left, mid1, mid2, right]))

    def test_min_heap_with_odd_length(self):
        for mid, *rest in [
            ((1, 2, 3, 4, 5)),
            ((2, 1, 3, 4, 5)),
            ((1, 3, 2, 4, 5)),
            ((3, 1, 2, 4, 5)),
            ((3, 2, 1, 4, 5)),
            ((5, 1, 2, 3, 4)),
            ((5, 2, 1, 3, 4)),
            ((5, 3, 1, 2, 4)),
            ((5, 3, 2, 1, 4)),
            ((5, 4, 1, 2, 3))
        ]:
            self.assertTrue(check_min_heap(mid + rest))

    def test_min_heap_with_even_length(self):
        for mid1, mid2, *rest in [
            ((1, 2, 3, 4, 5, 6)),
            ((2, 1, 3, 4, 5, 6)),
            ((1, 3, 2, 4, 5, 6)),
            ((3, 1, 2, 4, 5, 6)),
            ((3, 2, 1, 4, 5, 6)),
            ((6, 1, 2, 3, 4, 5)),
            ((6, 2, 1, 3, 4, 5)),
            ((6, 3, 1, 2, 4, 5)),
            ((6, 3, 2, 1, 4, 5)),
            ((6, 4, 1, 2, 3, 5)),
            ((6, 4, 2, 1, 3, 5)),
            ((6, 4, 3, 1, 2, 5)),
            ((6, 4, 3, 2, 1, 5)),
            ((6, 5, 1, 2, 3, 4))
        ]:
            self.assertTrue(check_min_heap(mid1 + mid2 + rest))

    def test_min_heap_with_max_index(self):
        for arr in [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [2, 1, 3, 4, 5, 6, 7, 8, 9],