import random


def max_min(min, max):
    """
    This function will return a Random integer between min and max.
    """
    #return 3
    return random.randint(int(min),int (max))


def Select_oeration():
    """This function will return a Random mathematical operation ."""
    return random.choice(['+', '-', '*'])


def Calculation(n1, n2, o):
    """we will take two random integers and random operation
     and we wil return the string of statement 'process_statement' and the result 'answer' """
    process_statement = f"{n1} {o} {n2}"

    if o == '+': answer = n1 + n2
    elif o == '-': answer = n1 - n2
    else: answer = n1 * n2
    return process_statement , answer

def math_quiz():
    """   in this function we will make few questions to user using loop and will give them their score"""
    # we will set the score =0
    score= 0
    #t_q = 3.14159265359
    total_questions = 3
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    # we will run the loop "total_questions" times
    for _ in range(total_questions):
        # we will take numbers in number1 and number2 and operator in operation
        number1 = max_min(1, 10); number2 = max_min(1, 5.5); operation = Select_oeration()

        PROBLEM, ANSWER = Calculation(number1, number2, operation)
        print(f"\nQuestion: {PROBLEM}")
        try:
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)
        except ValueError:
            print("Invalid answer .")

        else:
            if useranswer == ANSWER:
                print("Correct! You earned a point.")
                score += -(-1)
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
