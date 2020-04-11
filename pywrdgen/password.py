'''Represents a password that can be generated based on it's attributes.
'''


from random import sample

from string import (
    ascii_lowercase,
    ascii_uppercase,
    digits,
    punctuation,
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
        self._password = None
        self.char_set = ''
        self.alpha = kwargs['alpha']
        self.upper = kwargs['upper']
        self.numerals = kwargs['numerals']
        self.special = kwargs['special']
        self.length = kwargs['length']

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
            self._password = self.generate()
            return self._password
        else:
            return self._password


    def build_character_set(self):
        '''Assemble the list of acceptable characters for password generation.
        '''
        if self.alpha:
            self.char_set+= ascii_lowercase
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
        password = ''.join(sample(list(self.char_set), self.length))
        self._password = password
