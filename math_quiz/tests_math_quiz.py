import unittest
from math_quiz import max_min, Select_oeration, Calculation


class TestMathGame(unittest.TestCase):

    def test_function_max_min(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10

        for _ in range(1000):  # Test a large number of random values
            rand_num = max_min(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_oeration(self):
        # TODO
        add,subtract,multiply = '+','-','*'
        for _ in range(1000):  # Test a large number of random values
            operation = Select_oeration()
            self.assertTrue( operation == '+' or operation == '-' or operation == '*' )
        pass

    def test_function_Calculation(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 7, '+', '5 + 2', 12),
            (5, 2, '-', '5 + 2', 3),
            #TODO add more test cases here
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            result0 = Calculation(num1, num2, operator)
            result1 = result0[1]
            self.assertTrue(result1 == expected_answer)

if __name__ == "__main__":
    unittest.main()
