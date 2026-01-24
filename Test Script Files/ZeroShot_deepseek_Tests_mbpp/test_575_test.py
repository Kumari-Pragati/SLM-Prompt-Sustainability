import unittest
from mbpp_575_code import count_no

class TestCountNo(unittest.TestCase):

    def test_count_no_basic(self):
        self.assertEqual(count_no(2, 3, 2, 10), 6)

    def test_count_no_edge(self):
        self.assertEqual(count_no(1, 1, 1, 1), 1)

    def test_count_no_large(self):
        self.assertEqual(count_no(10, 10, 100, 200), 190)

    def test_count_no_zero(self):
        self.assertEqual(count_no(0, 1, 1, 10), 1)

    def test_count_no_negative(self):
        self.assertEqual(count_no(-1, 1, 1, 10), 1)

    def test_count_no_more_than_n(self):
        self.assertEqual(count_no(2, 5, 2, 10), 6)
