from distutils.core import setup

setup(
    name='Noqomo Currency Converter',
    version='0.1.0',
    author='Noqomo',
    author_email='noqomo@gmail.com',
    packages=['noq_py_currency-converter', 'noq_py_currency-converter.test'],
    scripts=[''],
    url='http://www.github.com/Noqomo/noq_py_currency-converter',
    license='LICENSE.txt',
    description='Simple currency conversion application.',
    long_description=open('README.txt').read(),
    install_requires=[
        "PySide >= 1.2.0",
        "PyQt >= 4.10.2",
    ],
)
