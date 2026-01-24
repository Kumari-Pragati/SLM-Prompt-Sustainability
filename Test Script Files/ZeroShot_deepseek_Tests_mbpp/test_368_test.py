import unittest
from mbpp_368_code import repeat_tuples

class TestRepeatTuples(unittest.TestCase):

    def test_repeat_tuples(self):
        self.assertEqual(repeat_tuples(('a', 'b'), 2), [('a', 'b'), ('a', 'b')])
        self.assertEqual(repeat_tuples(('1', '2', '3'), 3), [('1', '2', '3'), ('1', '2', '3'), ('1', '2', '3')])
        self.assertEqual(repeat_tuples(('x', 'y', 'z'), 1), [('x', 'y', 'z')])
        self.assertEqual(repeat_tuples((), 5), [(), (), (), (), ()])
        self.assertEqual(repeat_tuples(('p',), 0), [])
