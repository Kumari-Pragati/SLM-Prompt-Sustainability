import unittest
from mbpp_74_code import is_samepatterns

class TestIsSamePatterns(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertTrue(is_samepatterns(['red', 'green', 'blue'], ['#', '#', '#']))
        self.assertTrue(is_samepatterns(['red', 'red', 'red'], ['#', '#', '#']))

    def test_edge_conditions(self):
        self.assertFalse(is_samepatterns(['red', 'green'], ['#', '#', '#']))
        self.assertFalse(is_samepatterns(['red', 'green', 'blue'], ['#', '#']))
        self.assertFalse(is_samepatterns([], ['#']))
        self.assertFalse(is_samepatterns(['red', 'green', 'blue'], []))
        self.assertFalse(is_samepatterns([], []))

    def test_complex_cases(self):
        self.assertFalse(is_samepatterns(['red', 'green', 'blue'], ['#', '!', '#']))
        self.assertFalse(is_samepatterns(['red', 'red', 'blue'], ['#', '#', '#']))
        self.assertFalse(is_samepatterns(['red', 'green', 'blue'], ['#', '#', '!']))
