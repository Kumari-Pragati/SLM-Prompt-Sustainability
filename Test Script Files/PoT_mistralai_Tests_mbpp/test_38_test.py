import unittest
from mbpp_38_code import div_even_odd

class TestDivEvenOdd(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(div_even_odd([2, 4, 7, 8, 9]), 2.0)
        self.assertAlmostEqual(div_even_odd([1, 3, 4, 5, 6]), 1.0)
        self.assertAlmostEqual(div_even_odd([0, 1, 2, 3, 4]), 0.0)

    def test_edge_case_empty_list(self):
        self.assertAlmostEqual(div_even_odd([]), -1.0)

    def test_edge_case_single_element(self):
        self.assertAlmostEqual(div_even_odd([1]), -1.0)
        self.assertAlmostEqual(div_even_odd([2]), 1.0)

    def test_corner_case_mixed_order(self):
        self.assertAlmostEqual(div_even_odd([9, 4, 2, 7]), 45.0/9.0)
