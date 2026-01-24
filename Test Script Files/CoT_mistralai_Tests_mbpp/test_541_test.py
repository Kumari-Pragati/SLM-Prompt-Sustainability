import unittest
from mbpp_541_code import check_abundant

class TestCheckAbundant(unittest.TestCase):
    def test_abundant_numbers(self):
        self.assertTrue(check_abundant(12))
        self.assertTrue(check_abundant(28))
        self.assertTrue(check_abundant(496))

    def test_non_abundant_numbers(self):
        self.assertFalse(check_abundant(11))
        self.assertFalse(check_abundant(13))
        self.assertFalse(check_abundant(100))

    def test_edge_cases(self):
        self.assertFalse(check_abundant(1))
        self.assertTrue(check_abundant(math.ceil(math.sqrt(1000000))))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, check_abundant, 'a')
        self.assertRaises(TypeError, check_abundant, -1)
        self.assertRaises(TypeError, check_abundant, 0)
