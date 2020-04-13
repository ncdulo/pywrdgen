'''Represents a password that can be generated based on it's attributes.
'''


from pathlib import Path
from secrets import choice, randbelow
from string import (
    ascii_lowercase,
    ascii_uppercase,
    digits,
    punctuation,
    hexdigits,
)


class Password():
    def __init__(self, **kwargs):
        '''Create a new password object. Assign Password attributes based on
provided **kwargs, or defaults if missing.

  **kwargs:
    alpha -- include lowercase alphabetic characters [a-z]
    upper -- include uppercase alphabetic characters [A-Z]
    numerals -- include numerals [0-9]
    special -- include special characters ...'
    length -- total length, in characters, of generated password'
        '''
        self.debug = kwargs.get('debug')
        base_dir = Path(__file__).parent.resolve()
        self.word_file = Path(base_dir, 'data/eff_large_wordlist.txt')
        self.word_list= []
        self._password = None
        self.char_set = ''
        self.alpha = kwargs.get('alpha')
        self.upper = kwargs.get('upper')
        self.numerals = kwargs.get('numerals')
        self.special = kwargs.get('special')
        self.hexadecimal = kwargs.get('hexadecimal')
        self.want_passphrase = kwargs.get('passphrase')
        self.length = kwargs.get('length')

    def __str__(self):
        '''Return the generated password.'''
        return self.password

    def __repr__(self):
        '''Return a list of attributes that can be provided as **kwargs into
a new Password object. Seed is not currently supported, so new passwords
will not be exactly the same.
        '''
        pass

    @property
    def password(self):
        '''Getter method for password. Return the already generated password,
if one exists. Otherwise, generate a new one and return that.
        '''
        if self._password is None:
            #
            # REMOVE THIS -- Forced passphrase when `--debug` enabled
            #
            if self.debug:
                self.want_passphrase = True
            #
            # REMOVE THIS -- Forced passphrase when `--debug` enabled
            #
            if self.want_passphrase:
                self.generate_passphrase()
            else:
                self.generate()
            return self._password
        else:
            return self._password

    def build_character_set(self):
        '''Assemble the list of acceptable characters for password generation.
        '''
        if self.hexadecimal:
            # If hexadecimal output enabled, return early.
            # Use *only* hex in character set.
            # Do some manipulations here to remove lowercase `a-f`
            if self.upper:
                hexcase = hexdigits.upper()
            else:
                hexcase = hexdigits.lower()
            self.char_set += ''.join(list(set(hexcase)))
            return
        if self.alpha:
            self.char_set += ascii_lowercase
        if self.upper:
            self.char_set += ascii_uppercase
        if self.numerals:
            self.char_set += digits
        if self.special:
            self.char_set += punctuation

    def generate(self):
        '''Generate the password using instance attributes.'''
        # TODO: This needs much improvement. As is, there is no assurance
        # that we have at least one character from each selected character
        # set included. This will lessen strength of passwords.

        self.build_character_set()
        password = ''
        chars_remaining = self.length
        while chars_remaining > 0:
            password += choice(self.char_set)
            chars_remaining -= 1
        self._password = password

    def generate_passphrase(self):
        '''Generate a passphrase using instance attributes.'''
        self._password = ''

        # Load word list into memory (separate function?)
        self._load_word_list(self.word_file)

        # Using `--length` as the number of words, start creating them
        words_remaining = self.length
        while words_remaining > 0:
            word_index = ''
            # Yield over dice rolls to generate a numerical index, as
            # a string.
            for roll in self._roll_dice(5, 6):
                word_index += str(roll)
            # Find the line in our word list that contains the index
            line = [s for s in self._word_list if word_index in s]
            # Separate the cooresponding word from the line
            word = line[0].split('\t')[1].split('\n')[0]
            # Append the word, decrement counter
            self._password += word
            words_remaining -= 1

        # Transform, or add extra characters based on instance attributes

    def _load_word_list(self, word_file):
        '''Read the specified file into memory. One line in the file into
one line of text in `self._word_list`.'''
        with open(word_file, 'r') as fh:
            word_list = fh.readlines()
        self._word_list = word_list

    def _roll_dice(self, dice, value):
        '''Generate [dice]d[value] rolls and yield the results of each roll.
        '''
        for i in range(dice):
            yield randbelow(value-1)+1
