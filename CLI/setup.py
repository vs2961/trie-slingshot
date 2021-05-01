from setuptools import setup, find_packages

setup(
        name='Trie-CLI',
        version='1.0',
        scripts=['Trie-CLI'],
        author='Victor Siu',
        description='A CLI that calls a Electic Beanstalk server which supports \
                     Trie operations.',
        packages=find_packages(),
        include_package_data=True,
        install_requires=[
            'setuptools',
            'certifi >= 2020.12.5',
            'chardet >= 4.0.0',
            'idna >= 2.10',
            'requests >= 2.25.1',
            'urllib3 >= 1.26.4'
            ],
        python_requires='>=3.5',
        entry_points='''
            [console_scripts]
            commands=commands:cli
        ''',
)
