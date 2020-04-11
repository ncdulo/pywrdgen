'''Represents a password that can be generated based on it's attributes.
'''


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

    def generate(self):
        '''Generate the password using instance attributes.'''
        return 'iMaDe_THIS_p455w0rd!'
