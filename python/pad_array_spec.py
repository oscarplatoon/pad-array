# Write unit tests!
from pad_array import pad
import unittest # imports the Unit Test library

class PadTestCases(unittest.TestCase):

    def test_pad_1(self):
        output = pad([1,2,3], 5, 'apple')
        self.assertListEqual(output, [1,2,3,'apple', 'apple'])

    def test_pad_2(self):
        output = pad([1,2,3,4,5], 4)
        self.assertListEqual(output, [1,2,3,4,5])

    def test_pad_3(self):
        output = pad([], 4, '1')
        self.assertListEqual(output, ['1', '1', '1', '1'])

    def test_pad_4(self):
        output = pad([], 4)
        self.assertListEqual(output, [None, None, None, None])

if __name__ == '__main__':
    unittest.main()