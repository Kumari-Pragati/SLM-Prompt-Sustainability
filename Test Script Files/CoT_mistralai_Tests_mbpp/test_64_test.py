import unittest
from mbpp_64_code import subject_marks

class TestSubjectMarks(unittest.TestCase):

    def test_sorted_marks(self):
        data = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        result = subject_marks(data)
        expected = [('Maths', 97), ('Science', 90), ('English', 88), ('Social sciences', 82)]
        self.assertEqual(result, expected)

    def test_same_marks(self):
        data = [('English', 88), ('English', 88)]
        result = subject_marks(data)
        expected = [('English', 88), ('English', 88)]
        self.assertEqual(result, expected)

    def test_empty_list(self):
        data = []
        result = subject_marks(data)
        self.assertEqual(result, [])

    def test_single_subject(self):
        data = [('English', 88)]
        result = subject_marks(data)
        expected = [('English', 88)]
        self.assertEqual(result, expected)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            subject_marks(123)
