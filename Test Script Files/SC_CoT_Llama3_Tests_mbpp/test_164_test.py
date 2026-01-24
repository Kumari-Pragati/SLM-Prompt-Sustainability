import unittest
from mbpp_164_code import areEquivalent

class TestAreEquivalent(unittest.TestCase):
    def test_equivalent_numbers(self):
        self.assertTrue(areEquivalent(12, 24))
        self.assertTrue(areEquivalent(36, 48))
        self.assertTrue(areEquivalent(100, 200))

    def test_non_equivalent_numbers(self):
        self.assertFalse(areEquivalent(12, 13))
        self.assertFalse(areEquivalent(36, 37))
        self.assertFalse(areEquivalent(100, 101))

    def test_edge_cases(self):
        self.assertTrue(areEquivalent(1, 1))
        self.assertTrue(areEquivalent(2, 2))
        self.assertTrue(areEquivalent(3, 3))

    def test_divisible_by_1(self):
        self.assertTrue(areEquivalent(1, 2))
        self.assertTrue(areEquivalent(3, 6))
        self.assertTrue(areEquivalent(4, 8))

    def test_divisible_by_2(self):
        self.assertTrue(areEquivalent(2, 4))
        self.assertTrue(areEquivalent(6, 12))
        self.assertTrue(areEquivalent(8, 16))

    def test_divisible_by_3(self):
        self.assertTrue(areEquivalent(3, 9))
        self.assertTrue(areEquivalent(6, 18))
        self.assertTrue(areEquivalent(9, 27))

    def test_divisible_by_4(self):
        self.assertTrue(areEquivalent(4, 8))
        self.assertTrue(areEquivalent(8, 16))
        self.assertTrue(areEquivalent(12, 24))

    def test_divisible_by_5(self):
        self.assertTrue(areEquivalent(5, 10))
        self.assertTrue(areEquivalent(10, 20))
        self.assertTrue(areEquivalent(15, 30))

    def test_divisible_by_6(self):
        self.assertTrue(areEquivalent(6, 12))
        self.assertTrue(areEquivalent(12, 24))
        self.assertTrue(areEquivalent(18, 36))

    def test_divisible_by_7(self):
        self.assertTrue(areEquivalent(7, 14))
        self.assertTrue(areEquivalent(14, 28))
        self.assertTrue(areEquivalent(21, 42))

    def test_divisible_by_8(self):
        self.assertTrue(areEquivalent(8, 16))
        self.assertTrue(areEquivalent(16, 32))
        self.assertTrue(areEquivalent(24, 48))

    def test_divisible_by_9(self):
        self.assertTrue(areEquivalent(9, 18))
        self.assertTrue(areEquivalent(18, 36))
        self.assertTrue(areEquivalent(27, 54))

    def test_divisible_by_10(self):
        self.assertTrue(areEquivalent(10, 20))
        self.assertTrue(areEquivalent(20, 40))
        self.assertTrue(areEquivalent(30, 60))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            areEquivalent('a', 2)
        with self.assertRaises(TypeError):
            areEquivalent(2, 'b')
