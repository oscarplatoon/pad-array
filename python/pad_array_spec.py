from pad_array import pad
import unittest

class TestPad(unittest.TestCase):

    def test_for_ana(self):
        self.assertEqual(pad([1,2,3], 5, 'cat'), [1,2,3, 'cat', 'cat'])

    def test_for_no_new(self):
        self.assertEqual(pad([1,2,3], 0), [1,2,3])



if __name__ == '__main__':
    unittest.main()