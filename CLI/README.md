# CLI Details

Here, you will find instructions to install the CLI, as well as use it effectively.

## Prerequisites

You will need Python, install it using your local package manager or at https://www.python.org/downloads/

## Installation

1. Clone the repository, and navigate to the CLI folder, using `cd` for linux/unix and `dir` for windows.

2. _(Optional)_ Create and enter a virtual environment to test using the command `virtualenv venv`, then `source venv/bin/activate`

3. Run `pip install -e .` to install the command for the CLI. (**Note the . at the end**)

## Debugging

If you are missing packages, run `pip install -r requirements.txt` inside the CLI directory.

## How to use the CLI

You may use the built in help function using `Trie-CLI --help`, or just run `Trie-CLI`.

**Availiable Commands:**

* add           Adds STRING/the words in your file to the trie
* autocomplete  Returns a list of autocomplete suggestions based on your...
* delete        Deletes STRING from the trie
* display       Displays the Trie
* search        Tells you whether or not the keyword is in the Trie

Run `Trie-CLI [COMMAND] --help` for help with a specific command. (ex. `Trie-CLI add --help`)

## FAQ

***Can you provide example commands so that I understand how to use the CLI?***
Try `Trie-CLI add hello` and `Trie-CLI display`.

***Can I enter a prewritten word file?***
Use the -f, or --file flag to do so. (ex. `Trie-CLI add -f words.txt`)

***Your tree display implementation is cool!***
Thanks! I took inspiration from a tutorial for creating Directory Trees in Python. You can find it here: https://realpython.com/directory-tree-generator-python/#step-2-generating-a-directory-tree-diagram-in-python
