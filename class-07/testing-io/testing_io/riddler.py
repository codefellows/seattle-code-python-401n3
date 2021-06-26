class Riddler:
    
    def __init__(self, riddle='my favorite color', answer='green'):
        self.riddle = riddle
        self.answer = answer

    def play(self):
        print('What is your name?')
        name = input('> ')
        print(f'Hi, {name}. Let\'s get to guessing!')
        print(f'Step right up and guess {self.riddle}!')

        running = True

        while running:
            print('What is your guess?')
            guess = input('> ')
            if guess == self.answer:
                print('You got it!')
                running = False
            else:
                print('Nope, that\'s not it.')
