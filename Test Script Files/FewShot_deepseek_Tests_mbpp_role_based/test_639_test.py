import unittest
from mbpp_639_code import sample_nam

class TestSampleNam(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sample_nam(['Name1', 'name2', 'Name3']), 10)

    def test_edge_condition(self):
        self.assertEqual(sample_nam(['nAmE']), 4)

    def test_boundary_condition(self):
        self.assertEqual(sample_nam(['']), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sample_nam(123)

    def test_empty_list(self):
        self.assertEqual(sample_nam([]), 0)
