import unittest
from mbpp_38_code import div_even_odd

class TestDivEvenOdd(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(StopIteration):
            div_even_odd([])

    def test_single_element_list(self):
        self.assertAlmostEqual(div_even_odd([1]), 1.0)
        self.assertAlmostEqual(div_even_odd([2]), 2.0)

    def test_mixed_list(self):
        self.assertAlmostEqual(div_even_odd([1, 2, 3, 4, 5]), 2.0)
        self.assertAlmostEqual(div_even_odd([2, 1, 2, 3, 4]), 1.3333333333333337)

    def test_all_even_list(self):
        self.assertAlmostEqual(div_even_odd([2, 4, 6, 8]), 1.5)

    def test_all_odd_list(self):
        self.assertAlmostEqual(div_even_odd([1, 3, 5, 7, 9]), 0.5)

    def test_no_even_number(self):
        with self.assertRaises(StopIteration):
            div_even_odd([1, 3, 5, 7])
