import unittest
from pad_array import pad


class TestPad(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(pad([1, 2, 3], 5), [1, 2, 3, None, None])

    def test_case_2(self):
        self.assertEqual(pad([1, 2, 3], 5, 'apple'), [1, 2, 3, 'apple', 'apple']
                         )

    def test_case_3(self):
        self.assertEqual(pad([1, 2, 3], 3), [1, 2, 3]
                         )

    def test_case_4(self):
        self.assertEqual(pad([1, 2, 3], 1), [1, 2, 3]
                         )
