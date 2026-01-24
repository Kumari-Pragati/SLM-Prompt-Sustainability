import unittest
from mbpp_389_code import find_lucas

class TestFindLucas(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(find_lucas(0), 2)

    def test_one(self):
        self.assertEqual(find_lucas(1), 1)

    def test_small(self):
        self.assertEqual(find_lucas(2), 3)

    def test_negative(self):
        with self.assertRaisesRecursivedepth(10):
            find_lucas(-1)

    def test_large(self):
        self.assertEqual(find_lucas(10), 55)

    def test_invalid_type(self):
        with self.assertRaisesRecursivedepth(10):
            find_lucas("a")
