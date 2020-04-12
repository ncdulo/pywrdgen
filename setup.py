from setuptools import setup, find_packages
from os import path


# Read the README into memory, include into package info
cwd = path.abspath(path.dirname(__file__))
with open(path.join(cwd, 'README.md'), 'r') as fh:
    long_description = fh.read()


setup(name='pywrdgen',
      packages=find_packages(),
      version='0.1.0',
      author='ncdulo',
      license='MIT',
      url='https://github.com/ncdulo/pywrdgen',
      keywords='password pwgen generate generator cli utility tool',
      description='Generate (possibly) secure passwords.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      python_requires='>=3.6',
      install_requires=[
              'click',
          ],
      entry_points={
              'console_scripts': [
                  'pywrdgen = pywrdgen.__main__:main'
              ],
          },
      classifiers=[
              'Development Status :: 3 - Alpha',
              'Environment :: Console',
              'Intended Audience :: End Users/Desktop',
              'Intended Audience :: System Administrators',
              'License :: OSI Approved :: MIT License',
              'Natural Language :: English',
              'Operating System :: OS Independent',
              'Operating System :: POSIX :: Linux',
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3.6',
              'Programming Language :: Python :: 3.7',
              'Programming Language :: Python :: 3.8',
              'Programming Language :: Python :: 3 :: Only',
              'Topic :: Security',
              'Topic :: System :: Systems Administration',
              'Topic :: Utilities',
          ]
      )
