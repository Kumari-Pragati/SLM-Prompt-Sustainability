import unittest
from mbpp_541_code import check_abundant, get_sum

class TestCheckAbundant(unittest.TestCase):

    def test_check_abundant_positive(self):
        self.assertTrue(check_abundant(12))
        self.assertTrue(check_abundant(28))
        self.assertTrue(check_abundant(496))

    def test_check_abundant_zero(self):
        self.assertFalse(check_abundant(0))
        self.assertFalse(check_abundant(1))
        self.assertFalse(check_abundant(2))

    def test_check_abundant_negative(self):
        self.assertFalse(check_abundant(-1))
        self.assertFalse(check_abundant(-2))
        self.assertFalse(check_abundant(-100))

    def test_get_sum(self):
        self.assertEqual(get_sum(1), 0)
        self.assertEqual(get_sum(2), 0)
        self.assertEqual(get_sum(3), -3)
        self.assertEqual(get_sum(4), -3)
        self.assertEqual(get_sum(5), 0)
        self.assertEqual(get_sum(6), 0)
        self.assertEqual(get_sum(7), -7)
        self.assertEqual(get_sum(8), -3)
        self.assertEqual(get_sum(9), -9)
        self.assertEqual(get_sum(10), -3)
        self.assertEqual(get_sum(12), 0)
        self.assertEqual(get_sum(14), 2)
        self.assertEqual(get_sum(15), 0)
        self.assertEqual(get_sum(16), 0)
        self.assertEqual(get_sum(18), 2)
        self.assertEqual(get_sum(20), 4)
        self.assertEqual(get_sum(28), 14)
        self.assertEqual(get_sum(496), 240)
