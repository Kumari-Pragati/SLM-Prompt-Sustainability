import unittest
from mbpp_765_code import is_polite

class TestIsPolite(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(is_polite(1), 3)
        self.assertEqual(is_polite(2), 5)
        self.assertEqual(is_polite(10), 17)

    def test_zero(self):
        self.assertEqual(is_polite(0), 1)

    def test_negative_integer(self):
        self.assertEqual(is_polite(-1), 2)
        self.assertEqual(is_polite(-2), 4)

    def test_float(self):
        self.assertAlmostEqual(is_polite(2.5), 5.320308864)

    def test_edge_cases(self):
        self.assertEqual(is_polite(1e9), 100000001 + math.log(100000001 + math.log(100000001, 2), 2))
        self.assertEqual(is_polite(math.e), math.e + math.log(math.e + math.log(math.e, 2), 2))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, is_polite, 'string')
        self.assertRaises(TypeError, is_polite, None)
        self.assertRaises(TypeError, is_polite, [1, 2, 3])
