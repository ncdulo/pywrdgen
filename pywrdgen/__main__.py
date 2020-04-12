import click
from sys import argv

from pywrdgen.password import Password

CONTEXT_SETTINGS = {
        'help_option_names': ['-h', '--help'],
    }


#
# Main entry-point. Handles global flags, and info blurb.
#
@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version='0.0.1')
@click.pass_context
@click.option('-p', '--password-only',
              default=False,
              is_flag=True,
              help='outut only generated passwords')
@click.option('-d', '--debug',
              default=False,
              is_flag=True,
              help='include extra output text')
def main(ctx, **kwargs):
    '''Generate (possibly) secure passwords.'''

    # Pull the **kwargs flags out and into our context object. This will
    # be passed into sub-commands so they may access these global flags.
    ctx.obj = {
            'password_only': kwargs['password_only'],
            'debug': kwargs['debug'],
        }

    # Return early and skip the info message if password_only flag is enabled.
    if ctx.obj['password_only']:
        return

    print('pywrdgen')
    print('--------')
    print('Generate (possibly) secure passwords. By default, there are no')
    print('flags enabled in `gen` mode. You must enable some of them for a')
    print('password to be generated. The combination of options selected')
    print('form the baseline for how secure the generated password is.')
    print()
    print('There is no guarantee that any given generated password will be')
    print('secure or fit for any purpose. The ratings given are determined')
    print('based on your selected combination of options. Enjoy!')
    print()

#
# Password List Generation. Generates, and displays a list of passwords
# generated based on the flags set on the command line.
#
@main.command()
@click.pass_context
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
@click.option('-x', '--hexadecimal',
              default=False,
              is_flag=True,
              help='generate password in hexadecimal only [A-F0-9]')
@click.option('-l', '--length',
              default=0,
              type=int,
              help='length of password to generate, in characters')
@click.option('-c', '--count',
              default=0,
              type=int,
              help='number of passwords to generate, in total')
def gen(ctx, **kwargs):
    '''Generate a (possibly) secure password based on the specified options.'''
    if ctx.obj['debug']:
        for key, value in kwargs.items():
            print(f'{key}: {value}')
        print()

    # Create the new password object, providing it a **kwargs.
    passwords = []
    for i in range(kwargs['count']):
        p = Password(**kwargs)
        #p.generate()
        passwords.append(p)

    # Do some things to determine strength of password.
    # Based on options. Maybe also an algorithm to score it's randomness?

    # Output score, and (list of) passwords.
    if len(passwords) > 0:
        if not ctx.obj['password_only']:
            print(f'Generated {len(passwords)} passwords:')
        for password in passwords:
            print(password)
    # If no passwords generated
    else:
        # If we are *not* in password only mode, display an error message.
        if ctx.obj['password_only'] is False:
            print(
                'No password was generated. Please check the help text above.')
            print('The full list of generator flags is available with')
            print(f'{argv[0]} gen --help')


if __name__ == '__main__':
    main()
