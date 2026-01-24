import unittest
from mbpp_935_code import series_sum

class TestSeriesSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(series_sum(1), 1)

    def test_edge_case(self):
        self.assertEqual(series_sum(0), 0)

    def test_edge_case2(self):
        self.assertEqual(series_sum(-1), 0)

    def test_typical_case2(self):
        self.assertEqual(series_sum(2), 3)

    def test_typical_case3(self):
        self.assertEqual(series_sum(3), 6)

    def test_typical_case4(self):
        self.assertEqual(series_sum(4), 10)

    def test_typical_case5(self):
        self.assertEqual(series_sum(5), 15)

    def test_typical_case6(self):
        self.assertEqual(series_sum(6), 21)

    def test_typical_case7(self):
        self.assertEqual(series_sum(7), 28)

    def test_typical_case8(self):
        self.assertEqual(series_sum(8), 36)

    def test_typical_case9(self):
        self.assertEqual(series_sum(9), 45)

    def test_typical_case10(self):
        self.assertEqual(series_sum(10), 55)

    def test_edge_case3(self):
        with self.assertRaises(TypeError):
            series_sum("a")

    def test_edge_case4(self):
        with self.assertRaises(TypeError):
            series_sum(None)

    def test_edge_case5(self):
        with self.assertRaises(TypeError):
            series_sum([1, 2, 3])
