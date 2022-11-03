import random
import emoji


class Game_Hangman:
    def __init__(self):
        self.animals = ['lion', 'dog', 'cat']
        self.colours = ['red', 'blue', 'yellow']
        self.lives = 5
        self.animal_game = random.choice(self.animals)
        self.colour_game = random.choice(self.colours)
        self.repository = ['_'] * len(self.animal_game)

    def choose(self):
        self.choose_gamemode = input('Choose gamemode \nGamemodes:Animals,Colours :')
        print('-----Welcome To Hangman Game-----')
        print('lets play the game, rules are simple \nyou have to guess word, \nYou have 5 lives, Good Luck:)!')
        if self.choose_gamemode == 'Animals':
            print('Gamemode is Animals')
            return self.forAnimals()
        return 'gamemode is Colours'

    def forAnimals(self):
        starter = input('Input One Letter: ')

        if len(starter) > 1 or len(starter) == 0:
            print('only 1 letter')
            return self.forAnimals()

        if starter in self.animal_game:
            self.repository[self.animal_game.find(starter)] = starter
            print(self.repository)

            if '_' not in self.repository:
                print('You win!, that word was {}'.format(self.animal_game))
                self.try_again()
                self.choose()
            else:
                self.forAnimals()

        else:
            self.lives -= 1
            print('Incorrect letter, you have left {} lives'.format(self.lives))

            if self.lives == 4:
                for emj in range(1, 5):
                    emj += 1
                    print(emoji.emojize(":red_heart:", variant="emoji_type"), end="")
            elif self.lives == 3:
                for emj in range(1, 4):
                    emj += 1
                    print(emoji.emojize(":red_heart:", variant="emoji_type"), end="")
            elif self.lives == 2:
                for emj in range(1, 3):
                    emj += 1
                    print(emoji.emojize(":red_heart:", variant="emoji_type"), end="")
            elif self.lives == 1:
                for emj in range(1):
                    emj += 1
                    print(emoji.emojize(":red_heart:", variant="emoji_type"), end="")
            else:
                print('You Loose', emoji.emojize(':broken_heart:', variant='emoji_type'), end="")
            if self.lives == 0:
                self.try_again()

            return self.forAnimals()

    def try_again(self):
        chs = input('You Loose, Want To Play Again?, \nY/N: ')
        if chs == 'Y' or chs == 'y':
            self.choose()
        print('Good Bye')

    def forColours(self):
        repository = []
        for words in self.colour_game:
            repository.append(words)

        return repository




g = Game_Hangman()
print(g.choose())
