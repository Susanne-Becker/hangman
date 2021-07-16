import random
import cs50

class Lexicon:
    # initializer
    def __init__(self, length):
        assert length > 0 and length < 44 and length != 29, "Invalid word length for Lexicon"
        self.words = []

        # load the dictionary of words
        with open("dictionary.txt", "r") as f:
            for i in f:
                if len(i) == length:
                    self.words.append(i)

    # shuffle list and return random word
    def get_word(self):
        return(random.choice(self.words)) 


class Hangman:
    # initializer
    def __init__(self, word, number_guesses):
        self.word = word
        self.number_guesses = number_guesses
        self.guesses_left = number_guesses
        self.guesses = []
        self.current = ""


    # check if game still has to run
    def is_running(self):
        if self.guesses_left == 0 or self.won():
            return False
        else:
            return True

    # Check if guesses are valid
    def is_valid_guess(self, letter):
        if (letter.isalpha()) == False:
            print("You can only guess letters! >=(")
            return False
        if letter in self.guesses:
            print("You already guessed this letter! >=(")
            return False
        else:
            return True

    # check if guessed letter is in word
    def guess(self, letter):
	    assert len(letter) == 1 and self.is_valid_guess(letter)
	    self.guesses.append(letter)
	    self.guesses_left -= 1
	    for k in self.word:
	        if k == letter:
	            return True
	    else:
	        return False

    # make current pattern
    def current_pattern(self):
        self.current = ""
        for j in self.word:
            if j in self.guesses:
                self.current += j
            else:
                self.current += "_"
        return self.current


    # check if you win the game
    def won(self):
        if self.word == self.current:
            return True
        else:
            return False


def main():

    print("WELCOME TO HANGMAN ツ")

    # prompt and re-prompt for word length
    word_length = int(input('What length of word would you like to play with?\n'))
    while word_length > 44:
        word_length = int(input("No words are longer than 44 letters!\n"))

    # load words
    lexicon = Lexicon(word_length)

    # prompt and re-prompt for number of guesses
    number_guesses = int(input("How many guesses are allowed?\n"))
    while number_guesses <= 0:
        number_guesses = int(input("Negative or zero guesses make no sense.\n"))

    # run an infinite number of games
    while True:

        # game set-up
        print(f"I have a word in my mind of {word_length} letters.")
        word = lexicon.get_word()
        game = Hangman(word, number_guesses)

        # allow guessing and provide guesses to the game
        while game.is_running():

            # prompt and re-prompt for single letter
            letter = input(f"Guess a letter ({game.guesses_left} left): ")
            if len(letter) != 1 or not game.is_valid_guess(letter):
                continue

            # provide feedback
            if game.guess(letter):
                print("It's in the word! :))")
            else:
                print("That's not in the word :(")

            print(game.current_pattern())

        # after game ends, present the conclusion
        if game.won():
            print("Whoa, you won!!! Let's play again.")
        else:
            print(f"Sad, you lost ¯\_(ツ)_/¯. This was your word: {word}")

if __name__ == '__main__':
    main()