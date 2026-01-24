import unittest
from mbpp_172_code import count_occurance

class TestCountOccurance(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_occurance('sdt'), 1)
        self.assertEqual(count_occurance('sstdt'), 1)
        self.assertEqual(count_occurance('sdtstdt'), 2)

    def test_edge_cases(self):
        self.assertEqual(count_occurance(''), 0)
        self.assertEqual(count_occurance('s'), 0)
        self.assertEqual(count_occurance('st'), 0)
        self.assertEqual(count_occurance('dt'), 0)
        self.assertEqual(count_occurance('sdt'), 1)

    def test_corner_cases(self):
        self.assertEqual(count_occurance('sstdtstdt'), 2)
        self.assertEqual(count_occurance('sdtstdtstdt'), 3)
        self.assertEqual(count_occurance('sstdtstdtstdt'), 3)
        self.assertEqual(count_occurance('sdtstdtstdtstdt'), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_occurance(123)
        with self.assertRaises(TypeError):
            count_occurance(None)
        with self.assertRaises(TypeError):
            count_occurance(True)
        with self.assertRaises(TypeError):
            count_occurance(['s', 't', 'd'])
        with self.assertRaises(TypeError):
            count_occurance({'s': 't', 't': 'd'})
        with self.assertRaises(TypeError):
            count_occurance(('s', 't', 'd'))
