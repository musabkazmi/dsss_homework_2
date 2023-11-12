import unittest
from math_quiz import max_min, Select_oeration, Calculation


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = max_min(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def Select_oeration(self):
        # TODO
        add,subtract,multiply = '+','-','+'
        for _ in range(1000):  # Test a large number of random values
            operation = Select_oeration()
            self.assertTrue( operation , '+' or '-' or '*')
        pass

    def Calculation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 5, '+', '5 + 5', 10),
                ''' TODO add more test cases here '''
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                result = Calculation(num1,num2,operator)
                self.assertTrue(result, expected_answer)
                pass

if __name__ == "__main__":
    unittest.main()
