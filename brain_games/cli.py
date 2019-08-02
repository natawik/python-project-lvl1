import prompt


def run():
    name = prompt.string('May I have your name? ')
    greeting = "Hello, {}!"
    print(greeting.format(name))
    return(name)


question = "Question: {}"
# Shows a random number for game "is even?"
# Shows a random expression for game "calc"
# Shows a two random numbers for game "great common divisor"
# Shows a random progression with missing number for game "progression"


wrong_answer = "'{}' is wrong answer ;(. Correct answer was '{}'."


try_again = "Let's try again, {}!"
# If the user answered incorrectly.


correct_answer = "Congratulations, {}!"
# If all three answers are correct.
