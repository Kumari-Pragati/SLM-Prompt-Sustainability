import unittest
from mbpp_818_code import lower_ctr

class TestLowerCtr(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(lower_ctr("Hello"), 2)
        self.assertEqual(lower_ctr("hElLO"), 2)
        self.assertEqual(lower_ctr("hello WORLD"), 5)

    def test_edge_conditions(self):
        self.assertEqual(lower_ctr(""), 0)
        self.assertEqual(lower_ctr("12345"), 0)
        self.assertEqual(lower_ctr("@#$%^"), 0)

    def test_complex_cases(self):
        self.assertEqual(lower_ctr("hEllO WoRLD"), 4)
        self.assertEqual(lower_ctr("ALLCAPS"), 0)
        self.assertEqual(lower_ctr("lowercase"), 8)
        self.assertEqual(lower_ctr("MiXeD CaSe"), 3)
