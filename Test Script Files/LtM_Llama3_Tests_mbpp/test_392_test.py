import unittest
from mbpp_392_code import get_max_sum

class TestGetMaxSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(get_max_sum(1), 1)
        self.assertEqual(get_max_sum(2), 1)
        self.assertEqual(get_max_sum(3), 2)
        self.assertEqual(get_max_sum(4), 3)
        self.assertEqual(get_max_sum(5), 4)
        self.assertEqual(get_max_sum(6), 6)

    def test_edge(self):
        self.assertEqual(get_max_sum(0), 0)
        self.assertEqual(get_max_sum(1), 1)
        self.assertEqual(get_max_sum(2), 2)
        self.assertEqual(get_max_sum(3), 3)
        self.assertEqual(get_max_sum(4), 4)
        self.assertEqual(get_max_sum(5), 5)

    def test_max(self):
        self.assertEqual(get_max_sum(10), 10)
        self.assertEqual(get_max_sum(20), 20)
        self.assertEqual(get_max_sum(30), 30)
        self.assertEqual(get_max_sum(40), 40)
        self.assertEqual(get_max_sum(50), 50)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            get_max_sum(-1)
        with self.assertRaises(TypeError):
            get_max_sum(None)
