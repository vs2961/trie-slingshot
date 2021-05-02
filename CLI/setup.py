from setuptools import setup

setup(
    name='Trie-CLI',
    version='1.0',
    author='Victor Siu',
    description='A CLI that calls a Electic Beanstalk server which supports \
                 Trie operations.',
    py_modules=['commands'],
    install_requires=[
        'setuptools',
        'requests >= 2.25.1',
        'click >= 7.1.2',
        'pytest >= 6.2.3'
    ],
    python_requires='>=3.5',
    entry_points='''
        [console_scripts]
        Trie-CLI=commands:cli
    ''',
)
