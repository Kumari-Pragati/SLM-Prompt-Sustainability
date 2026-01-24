import unittest
from mbpp_38_code import div_even_odd

class TestDivEvenOdd(unittest.TestCase):

    def test_div_even_odd(self):
        self.assertEqual(div_even_odd([1, 2, 3, 4]), 2/1)
        self.assertEqual(div_even_odd([1, 3, 5, 7]), -1)
        self.assertEqual(div_even_odd([2, 4, 6, 8]), -1)
        self.assertEqual(div_even_odd([1, 3, 5, 7, 2, 4, 6, 8]), 2/1)
        self.assertEqual(div_even_odd([1]), -1)
        self.assertEqual(div_even_odd([]), -1)
