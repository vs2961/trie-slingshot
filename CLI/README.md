# CLI Details

Here, you will find instructions to install the CLI, as well as use it effectively.

## Prerequisites

You will need Python, install it using your local package manager or at https://www.python.org/downloads/

## Installation

1. Clone the repository, and navigate to the CLI folder, using `cd` for linux/unix and `dir` for windows.

2. _(Optional, but recommended)_ Create and enter a virtual environment to test using the command `virtualenv venv`, then `source venv/bin/activate`

3. Inside the CLI folder, run `pip install -e .` to install the command for the CLI. (**Note the . at the end**)


## Debugging

* If you are missing packages, run `pip install -r requirements.txt` inside the CLI directory.

* You can exit the virtual environment you created in step 2 of installation with `deactivate`

## How to use the CLI

You may use the built in help function using `Trie-CLI --help`, or just run `Trie-CLI`.

**Availiable Commands:**
Command       | Description
------------- | -------------
add           | Adds the keyword(s)/words in your file to the trie
autocomplete  | Returns a list of autocomplete suggestions based on your keyword
delete        | Deletes the keyword(s)/words in your file from the trie
display       | Displays the Trie
search        | Tells you whether or not the keyword is in the Trie
drop\_db      | Deletes all nodes from the Trie

Run `Trie-CLI [COMMAND] --help` for help with a specific command. (ex. `Trie-CLI add --help`)

## Using the Testing Suite

1. Before using the Testing Suite, you must clear the table. Type `Trie-CLI drop_db --yes`.

2. Navigate into the `testing_suite` folder and run `pytest test.py`. This will run basic tests on the Trie. See the file for more information.

3. To test the global state of the trie, I've provided a file `global_test.py` with basic commands. I've marked where you can edit to add more tests.

## FAQ

***Can you provide example commands so that I understand how to use the CLI?*** <br />
Try `Trie-CLI add hello world` and `Trie-CLI display`.
This adds the words hello and world, and displays them in the trie.

***Can I enter a prewritten word file?*** <br />
Use the -f, or --file flag to do so. (ex. `Trie-CLI add -f words.txt`)

***Your tree display implementation is cool!*** <br />
Thanks! I took inspiration from a [tutorial](https://realpython.com/directory-tree-generator-python/#step-2-generating-a-directory-tree-diagram-in-python) for creating Directory Trees in Python.
