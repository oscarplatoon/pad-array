from pad_array import pad
import unittest

class TestStringMethods(unittest.TestCase):

    def test_output(self):
        output = pad([1,2,3,4],5, value = 'extra num')
        self.assertEqual(output, [1,2,3,4, 'extra num'])

    def test_list(self):
        output = type(pad([1,2,3,4],5, value = 'extra num'))       
        self.assertEqual(output, list)
        

    def test_len(self):
        output = len(pad([1,2,3,4],5, value = 'extra num'))
        self.assertEqual(output, 5)

if __name__ == '__main__':
    unittest.main()