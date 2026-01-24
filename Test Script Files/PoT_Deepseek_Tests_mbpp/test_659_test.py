import unittest
from mbpp_659_code import Repeat

class TestRepeat(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Repeat([1, 2, 2, 3, 4, 4, 4]), [2, 4])

    def test_empty_list(self):
        self.assertEqual(Repeat([]), [])

    def test_single_element(self):
        self.assertEqual(Repeat([1]), [])

    def test_all_repeated_elements(self):
        self.assertEqual(Repeat([1, 1, 1, 1]), [1])

    def test_no_repeated_elements(self):
        self.assertEqual(Repeat([1, 2, 3, 4]), [])

    def test_repeated_elements_at_start(self):
        self.assertEqual(Repeat([1, 1, 2, 2]), [1, 2])

    def test_repeated_elements_at_end(self):
        self.assertEqual(Repeat([2, 2, 3, 3]), [2, 3])

    def test_repeated_elements_in_middle(self):
        self.assertEqual(Repeat([1, 2, 2, 3]), [2])
