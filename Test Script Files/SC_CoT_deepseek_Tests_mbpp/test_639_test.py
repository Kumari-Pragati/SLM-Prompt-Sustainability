import unittest
from mbpp_639_code import sample_nam

class TestSampleNam(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sample_nam(['Abc', 'def', 'GHI']), 9)

    def test_edge_case(self):
        self.assertEqual(sample_nam(['aBc', 'dEf', 'gHi']), 0)

    def test_corner_case(self):
        self.assertEqual(sample_nam(['AbC', 'dEf', 'GHI']), 9)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sample_nam(123)
