import unittest
from mbpp_519_code import volume_tetrahedron

class TestVolumeTetrahedron(unittest.TestCase):

    def test_positive_integer(self):
        """Test volume calculation for positive integers"""
        for num in [1, 2, 5, 10]:
            result = volume_tetrahedron(num)
            self.assertAlmostEqual(result, (num ** 3 / (6 * math.sqrt(2))), delta=0.01)

    def test_zero(self):
        """Test volume calculation for zero"""
        result = volume_tetrahedron(0)
        self.assertEqual(result, 0)

    def test_negative_integer(self):
        """Test volume calculation for negative integers"""
        for num in [-1, -2, -5, -10]:
            result = volume_tetrahedron(num)
            self.assertEqual(result, 0)

    def test_float(self):
        """Test volume calculation for floats"""
        for num in [1.5, 2.5, 5.5, 10.5]:
            result = volume_tetrahedron(num)
            self.assertAlmostEqual(result, (num ** 3 / (6 * math.sqrt(2))), delta=0.01)

    def test_large_number(self):
        """Test volume calculation for large numbers"""
        large_num = 1000
        result = volume_tetrahedron(large_num)
        self.assertGreater(result, 1000000)
