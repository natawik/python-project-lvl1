import prompt


def run():
    name = prompt.string('May I have your name? ')
    greeting = "Hello, {}!"
    print(greeting.format(name))
