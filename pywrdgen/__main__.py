import click

from pywrdgen.password import Password

DEBUG = True

CONTEXT_SETTINGS = {
        'help_option_names': ['-h', '--help'],
    }


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version='0.0.1')
def pwgen():
    '''Generate (possibly) secure passwords.'''
    print('pwgen!')
    print('------')
    print('Generate (possibly) secure passwords. By default, there are no')
    print('flags enabled in `gen` mode. You must enable some of them for a')
    print('password to be generated. The combination of options selected')
    print('form the baseline for how secure the generated password is.')
    print()
    print('There is no guarantee that any given generated password will be')
    print('secure or fit for any purpose. The ratings given are determined')
    print('based on your selected combination of options. Enjoy!')
    print()


@pwgen.command()
@click.option('-a', '--alpha',
    default=False,
    is_flag=True,
    help='include lowercase alphabetic characters [a-z]')
@click.option('-u', '--upper',
    default=False,
    is_flag=True,
    help='include uppercase alphabetic characters [A-Z]')
@click.option('-n', '--numerals',
    default=False,
    is_flag=True,
    help='include numerals [0-9]')
@click.option('-s', '--special',
    default=False,
    is_flag=True,
    help='include special characters [LIST THEM HERE -- DYNAMICALLY]')
@click.option('-l', '--length',
    default=0,
    type=int,
    help='length of password to generate, in characters')
@click.option('-c', '--count',
    default=0,
    type=int,
    help='number of passwords to generate, in total')
def gen(**kwargs):
    '''Generate a (possibly) secure password based on the specified options.'''
    print('generating!')
    if DEBUG:
        for key, value in kwargs.items():
            print(f'{key}: {value}')
        print()

    # Create the new password object, providing it a **kwargs.
    passwords = []
    for i in range(kwargs['count']):
        #passwords.append(f'generated password #{password}')
        p = Password(**kwargs)
        p.generate()
        passwords.append(p)
    
    # Do some things to determine strength of password.
    # Based on options. Maybe also an algorithm to score it's randomness?

    # Output score, and (list of) passwords.
    if len(passwords) > 0:
        for password in passwords:
            print(password)
    else:
        print('No password was generated. Please check the help text above.')

if __name__ == '__main__':
    pwgen()
