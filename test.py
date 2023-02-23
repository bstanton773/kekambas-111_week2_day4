from whiteboard import solution
from unittest import TestCase


class TestWhiteboard(TestCase):

    def test_1_fifteen(self):
        # Test case 1: Input of 15
        expected_output = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7,
                           8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
        self.assertEqual(solution(15), expected_output)

    def test_2_ten(self):
        # Test case 2: Input of 10
        expected_output = [1, 2, 'Fizz', 4,
                           'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']
        self.assertEqual(solution(10), expected_output)

    def test_3_twenty(self):
        # Test case 3: Input of 20
        expected_output = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz',
                           'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz']
        self.assertEqual(solution(20), expected_output)

    def test_4_one(self):
        # Test case 4: Input of 1
        expected_output = [1]
        self.assertEqual(solution(1), expected_output)


