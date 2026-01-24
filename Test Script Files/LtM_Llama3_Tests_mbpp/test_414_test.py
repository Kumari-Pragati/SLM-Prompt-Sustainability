import unittest
from mbpp_414_code import overlapping

class TestOverlapping(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(overlapping([],[]), 0)
    def test_single_element_lists(self):
        self.assertEqual(overlapping([1],[]), 0)
        self.assertEqual(overlapping([],[1]), 0)
    def test_no_common_elements(self):
        self.assertEqual(overlapping([1,2,3],[4,5,6]), 0)
    def test_common_elements(self):
        self.assertEqual(overlapping([1,2,3],[2,3,4]), 1)
    def test_common_elements_at_start(self):
        self.assertEqual(overlapping([1,2,3],[1,2,3]), 1)
    def test_common_elements_at_end(self):
        self.assertEqual(overlapping([1,2,3,4],[1,2,3]), 1)
    def test_common_elements_in_middle(self):
        self.assertEqual(overlapping([1,2,3,4,5],[2,3,4]), 1)
    def test_common_elements_at_start_and_end(self):
        self.assertEqual(overlapping([1,2,3,4,5],[1,2,3,4]), 1)
