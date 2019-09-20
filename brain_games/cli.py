import prompt


def greet():
    name = prompt.string('May I have your name? ')
    greeting = "Hello, {}!"
    print(greeting.format(name))
    return name


QUESTION = "Question: {}"
# Shows a random number for games "even" or "prime"
# Shows a random expression for game "calc"
# Shows a two random numbers for game "great common divisor"
# Shows a random progression with missing number for game "progression"


WRONG_ANSWER = "'{}' is wrong answer ;(. Correct answer was '{}'."


TRY_AGAIN = "Let's try again, {}!"
# If the user answered incorrectly.


CORRECT_ANSWER = "Congratulations, {}!"
# If all three answers are correct.
