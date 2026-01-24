import unittest
from mbpp_659_code import Repeat

class TestRepeat(unittest.TestCase):

    def test_repeat_empty_list(self):
        self.assertEqual(Repeat([]), [])

    def test_repeat_single_element(self):
        self.assertEqual(Repeat([1]), [])

    def test_repeat_no_repeat(self):
        self.assertEqual(Repeat([1, 2, 3, 4]), [])

    def test_repeat_all_repeat(self):
        self.assertEqual(Repeat([1, 1, 1, 1]), [1])

    def test_repeat_some_repeat(self):
        self.assertEqual(Repeat([1, 2, 2, 3]), [2])

    def test_repeat_complex_list(self):
        self.assertEqual(Repeat([1, 2, 3, 2, 1]), [1, 2])
