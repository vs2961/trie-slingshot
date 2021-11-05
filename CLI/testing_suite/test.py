"""
Use this file to test the basic capabilities of the Trie.

Display not included in testing suite because it is more of a visual test.

For all tests to pass, the database must be empty. Run "Trie-CLI drop-db --yes"
to clear the database.

"""

import subprocess


def add(to_add, isFile=False):
    if type(to_add) == str:
        to_add = [to_add]
    if isFile:
        return subprocess.run(["Trie-CLI", "add", "-f"] + to_add,
                              stdout=subprocess.PIPE, text=True)
    return subprocess.run(["Trie-CLI", "add"] + to_add,
                          stdout=subprocess.PIPE, text=True)


def delete(to_delete, isFile=False):
    if type(to_delete) == str:
        to_delete = [to_delete]
    if isFile:
        return subprocess.run(["Trie-CLI", "delete", "-f"] + to_delete,
                              stdout=subprocess.PIPE, text=True)
    return subprocess.run(["Trie-CLI", "delete"] + to_delete,
                          stdout=subprocess.PIPE, text=True)


def search(to_search, isFile=False):
    return subprocess.run(["Trie-CLI", "search", to_search],
                          stdout=subprocess.PIPE, text=True)


def autocomplete(to_autocomplete):
    return subprocess.run(["Trie-CLI", "autocomplete", to_autocomplete],
                          stdout=subprocess.PIPE, text=True)


# 1st test: Add the word "hello", search for it, then delete it.
def test_add_find_delete():
    add("hello")
    hello_exists = search("hello").stdout
    assert hello_exists == "True\n"
    delete("hello")
    hello_exists = search("hello").stdout
    assert hello_exists == "False\n"


# 2nd test: Add the word "hello", search its substrings, then delete it.
def test_substrings():
    add("hello")
    for i in range(len("hello")):
        sub_exists = search("hello"[:i + 1]).stdout
        if i + 1 < len("hello"):
            # Any substring from [0, i] that is not "hello"
            assert sub_exists == "False\n"
        else:
            # The full string "hello"
            assert sub_exists == "True\n"
    delete("hello")


# 3rd test: Test if autocomplete is working properly.
def test_autocomplete():
    # Note the two "telephone"
    add(["telemarketer", "telephone", "telephone", "tele", "phone"])
    words = autocomplete("tele").stdout.strip()
    assert len(words.split("\n")) == 3  # tele, telephone, telemarketer

    # Here, we only need to delete telephone once
    delete(["telemarketer", "telephone", "tele", "phone"])


# 4th test: Load testing: We use a giant file word_test.txt to test our trie
def test_file():
    # word_test.txt contains 500 words.
    add("word_test.txt", isFile=True)
    delete("word_test.txt", isFile=True)
    all_words = autocomplete("").stdout
    assert all_words == "No words detected.\n"


# Add tests after this line
test_add_find_delete()
test_substrings()
test_autocomplete()
test_file()
