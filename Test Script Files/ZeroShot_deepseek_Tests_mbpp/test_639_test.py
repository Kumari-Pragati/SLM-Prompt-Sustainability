import unittest
from mbpp_639_code import sample_nam

class TestSampleNam(unittest.TestCase):

    def test_sample_nam(self):
        self.assertEqual(sample_nam(['Name', 'name', 'nAmE']), 5)
        self.assertEqual(sample_nam(['N', 'n', 'Na']), 1)
        self.assertEqual(sample_nam(['nAmE', 'NaMe', 'nAmE']), 0)
        self.assertEqual(sample_nam(['Name1', 'name2', 'nAmE3']), 0)
        self.assertEqual(sample_nam(['N1', 'n2', 'N3']), 0)
