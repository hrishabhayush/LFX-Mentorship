import program
import unittest

class TestInnovateList(unittest.TestCase):
    '''A class containing all the methods needed to test innovateList function'''
    def test_valid_input(self):
        '''
        Tests the function innovateList for valid inputs.

        When the length of the input list is a multiple of 10, the function cross checks against
        the returned list.
        '''
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        result = program.innovateList(input_list)
        self.assertListEqual(result, [2, 6, 8, 12, 14, 18, 20])

    def test_invalid_length(self):
        '''
        Tests the function innovateList for valid inputs.

        When the length of the input list is not a multiple of 10, the function 
        should print an error message. 
        '''
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        with self.assertRaises(ValueError) as context:
            program.innovateList(input_list)
        self.assertEqual(str(context.exception), "Input list is not a multiple of 10")

    def test_empty_input(self):
        '''
        Tests the case of empty list.
        '''
        input_list = []
        result = program.innovateList(input_list)
        self.assertListEqual(result, [])

if __name__ == '__main__':
    unittest.main()