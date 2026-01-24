import unittest
from mbpp_512_code import namedtuple
from 512_code import count_element_freq, flatten

TestTuple = namedtuple('TestTuple', 'test_tuple, expected_freq_dict')

class TestCountElementFreq(unittest.TestCase):

    test_cases = [
        TestTuple(
            ((1, 2, (3, 4)), {1: 1, 2: 1, 3: 1, 4: 1}),
            ((1, 1, 2, 2, 3, 3, 4, 4), {1: 2, 2: 2, 3: 2, 4: 2}),
            ((1, 2, 2, 1, 2, 1), {1: 3, 2: 3}),
            ((1, 2, 3, 2, 1, 2, 3, 1), {1: 3, 2: 3, 3: 2})
        )
    ]

    def test_count_element_freq(self):
        for test_case in self.test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(count_element_freq(test_case.test_tuple), test_case.expected_freq_dict)
