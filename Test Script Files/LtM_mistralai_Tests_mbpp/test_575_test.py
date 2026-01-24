import unittest
from mbpp_575_code import count_no

class TestCountNo(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(count_no(2, 3, 1, 5), 4)
        self.assertEqual(count_no(3, 2, 1, 5), 5)
        self.assertEqual(count_no(5, 1, 1, 5), 5)

    def test_edge_and_boundary(self):
        self.assertEqual(count_no(2, 1, 1, 2), 2)
        self.assertEqual(count_no(2, 1, 2, 2), 2)
        self.assertEqual(count_no(2, 1, 1, 0), 0)
        self.assertEqual(count_no(2, 1, 6, 10), 6)
        self.assertEqual(count_no(2, 1, 1, 1000), 1000)

    def test_complex(self):
        self.assertEqual(count_no(2, 3, 100, 200), 150)
        self.assertEqual(count_no(3, 2, 100, 200), 199)
        self.assertEqual(count_no(5, 1, 100, 200), 100)
